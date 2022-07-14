from dataset import Dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import config
import mysql.connector
import sqlalchemy

# def connect_to_mysql(hostname, username, password, database):
#     db = mysql.connector.connect(host="localhost", user="root", passwd=<password>, database="database_test")
#     return db

# Parameters
hostname = config.hostname
username = config.username
pwd = config.password
database = config.database
link = "https://www2.cs.arizona.edu/classes/cs120/fall17/ASSIGNMENTS/assg02/Pokemon.csv"


# creates sqlalchemy engine - uses sqlalchemy to connect to mysql db instance
def create_engine(hostname, username, password, database):
    # create engine
    engine = sqlalchemy.create_engine("mysql://" + username + ":" + password + "@" + hostname + "/" + database)
    # connect to engine
    sqlalchemy_engine_connection = engine.connect()
    return sqlalchemy_engine_connection


# returns a dataframe from a particular link
def create_df(data_link):
    dataset = Dataset(data_link, delimiter=',', header=0)
    dataframe = pd.DataFrame(data=dataset.features, columns=dataset.feature_names)
    return dataframe


# loads a dataframe into the mysql db connection
def df_to_mysql(connection_engine, df):
    df.to_sql(con=connection_engine, name='pokemon_data', if_exists='replace', index=False)


# RUN
# first connect to mysql db instance
connection = create_engine(hostname, username, pwd, database)
# create the dataframe that is to be loaded
df = create_df(link)
# loads data frame into mysql db instance
df_to_mysql(connection, df)

print(df)

connection.close()

# TODO: Connect to PowerBI from this mysql database
# TODO: Run some visualizations on this data
# TODO: Create tests/test suite with the current code
