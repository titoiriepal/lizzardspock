import json
import os
import platform


def loadfile(filePath):
    try:
        with open(filePath) as file:
            data = json.load(file)
    except FileNotFoundError:
        print('The file you want to upload does not exist')
        exit()
    return data


def saveFile(data, filePath):
    try:
        with open(filePath, 'w') as output:
            json.dump(data, output, indent=4)
    except FileNotFoundError:
        with open(filePath, 'w') as output:
            json.dump(data, output, indent=4)
