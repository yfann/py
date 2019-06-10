import os
import json

input = 'C:/Data/aggregate_data_6_6.json'
output = 'C:/Data/aggregate_data_6_6_output.json'

def processFile(file):
    for line in open(file,'r',encoding="utf8"):
        processLine(line)

def processLine(line):
    data=json.loads(line)
    with open(output, 'a') as f:
        f.write(json.dumps(data["_source"])+'\n')


processFile(input)