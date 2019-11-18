import json

with open ("C:/JSON/pyemp.json",'r') as fs:
    data = json.load(fs)
    
    for i in data:
        for key, value in i.items():
            print(f"{key} {value}")
        print('-'* 60)

