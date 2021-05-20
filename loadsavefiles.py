import json
import os
import platform

OPTIONS = ('Y', 'N')


def loadfile(filePath):
    try:
        with open(filePath) as file:
            data = json.load(file)
    except FileNotFoundError:
        print('The file you want to upload does not exist')
        exit()
    except json.decoder.JSONDecodeError:
        deleteFile = 'a'
        while deleteFile not in OPTIONS:
            deleteFile = input('The file you want to upload has corrupted. ¿Do you want to delete it? y/n: ')
            deleteFile = deleteFile.upper()
            if deleteFile == 'Y':
                if platform.system() == 'Windows':
                    instruction = "del " + filePath
                    os.system(instruction)
                elif platform.system() == 'Linux':
                    instruction = "rm " + filePath
                    os.system(instruction)
                print('Restart the aplication, please')
                exit()
            elif deleteFile == 'N':
                print('No options have been made on the file')
                exit()
    return data


def saveFile(data, filePath):
    try:
        with open(filePath, 'w') as output:
            json.dump(data, output, indent=4)
    except FileNotFoundError:
        with open(filePath, 'w') as output:
            json.dump(data, output, indent=4)
