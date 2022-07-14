import json

#utility that loads a .json config file and returns a python dictionary of that file
def load_config(filename):
    # open a json config file
    if '.json' in filename:
        # have to open json config file to load
        # json.load() returns JSON object as a dictionary
        jsonfile = json.load(open(filename))
        #return json object as dictionary
        return jsonfile
    else:
        return "error: not a .json file passed as parameter"
