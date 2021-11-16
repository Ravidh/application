from glob import glob
import json

def p_list(path,input="all"):
    '''

    This function recieves a path to a directory,
    reads all the JSON files in the directory
    and returns a list of the names of the JSON files.
    '''

    file_list = glob(path+'*.json')
    names = []
    info = []

    for f in file_list:

        file = open(f,"r")
        data = json.load(file)

        names.append(data['name'])
        info.append(data)

    if input == "all":
        return names, info

    else:
        firstup = input[0].upper()
        if len(input)>1:
            firstup = firstup+input[1:]
        part_names = [n for n in names if (input in n) | (input.upper() in n) | (input.lower() in n) | (firstup in n)]
        part_info = [i for i in info if (input in i["name"]) | (input.upper() in i["name"]) | (input.lower() in i["name"]) | (firstup in i["name"])]

        if len(part_names)>0:
            return part_names, part_info
        else:
            return names, []
