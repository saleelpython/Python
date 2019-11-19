import pymongo
person={"_id": 2, "name":"ram"}
try:
    mongoDBClient = pymongo.MongoClient(host='192.168.100.20', port=27017)
    db = mongoDBClient['primaryDB']
    print(f'Collection List in {db.name} {db.list_collection_names()}')
    
except pymongo.errors.DuplicateKeyError as ex:
    print(f'pymongo.errors.DuplicateKeyError : {ex}')

except pymongo.errors.CollectionInvalid as ex:
    print(f'pymongo.errors.CollectionInvalid : {ex}')

finally:
    print()
    print('-'  * 40 ,' ', sep="\n")
    print("Document inserted!")
