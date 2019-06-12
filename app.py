import json

with open('Superstore.json') as p:
    data = json.load(p)

# for i in range(0, len(data)):
#     print(f"Document {i}")
#     print();
#     for key, value in data[i].items():
#         print(f"{key} : {value}")
#     print();
#     print("-----------------------------------")


def getRegion(d):
    if d['Region'] in "West":
        return True
    else:
        return False

r = list(filter(getRegion, data))

for i in range(0, len(r)):
    print(f"Document {i}")
    print(r[i]['Row ID'])
    print(r[i]['Order ID'])
    print(r[i]['Order Date'])
    print((r[i]['Region']))

    print("-----------------------------")