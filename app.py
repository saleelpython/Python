import json
import pymongo


with open("person.json", 'r') as fs:
    data = json.load(fs)

try:
    mongoDBClient = pymongo.MongoClient(host='192.168.100.20', port = 27017)

    db = mongoDBClient.get_database('primaryDB')

    # collection = db.get_collection('empq')
    collection = db['per']
    print(f'"db" : "{db.name}" - "collection" : "{collection.name}"')
    print('-' * 42)

    for i in data:
        collection.insert_one(i)
       

except pymongo.errors.DuplicateKeyError as ex:
    # print(list(ex.))
    print(f'Error Code : {ex.code} \n\nMessage : {ex.args}')

except pymongo.errors.CollectionInvalid as ex:
    print(f'pymongo.erro {ex}')

finally:
    print()
    print()
    print()
    print(f'Done')