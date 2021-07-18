import json

filename = ".../data/glove.6B.100d.txt"

dict1 = {}

with open(filename) as fh:
  
    for line in fh:
  
        # reads each line and trims of extra the spaces 
        # and gives only the valid words
        command, description = line.strip().split(None, 1)
  
        dict1[command] = description.strip()
  
# creating json file
# the JSON file is named as test1
out_file = open("glove_6B_100d.json", "w")
json.dump(dict1, out_file, sort_keys = False)
out_file.close()
