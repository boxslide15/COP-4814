import json

def save_to_file(filename, data):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file, indent = 4)
        print("The file {0} was successfully created.".format(filename))

def read_from_file(filename):
    with open(filename, "r") as read_file:
        jsonData = json.load(read_file)
        print("The file {0} was successfully read.".format(filename))
        return jsonData