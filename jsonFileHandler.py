import json
def readJsonFile(fileName):
    data = ""
    try:
        with open ('files/insulin.json') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
        