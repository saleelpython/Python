import module2

person = [
    {"_id":1, "indexID": "1001", "firstName": "Saleel", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
    {"_id":2,"indexID": "1002", "firstName": "Vrushali", "lastName": "Bagde", "canVote": "True", "canDrive": "False"}, 
    {"_id":3,"indexID": "1003", "firstName": "Sharmin", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
    {"_id":4,"indexID": "1004", "firstName": "Nitish", "lastName": "Patil", "canVote": "True", "canDrive": "True"}, 
    {"_id":5,"indexID": "1005", "firstName": "Neel", "lastName": "Save", "canVote": "False", "canDrive": "True"}, 
    {"_id":6,"indexID": "1006", "firstName": "Deep", "lastName": "Save", "canVote": "False", "canDrive": "False"}, 
    {"_id":7,"indexID": "1007", "firstName": "Ruhan", "lastName": "Bagde", "canVote": "False", "canDrive": "False"}
]

def getPerson(l):
    for i in l:
        yield i
            
b =  getPerson(person)

# while (x := input("Continue?")) == 'y' or 'Y':
#     print("Good")


# while (y := int(input("Continue?"))) == 1 or 2:
#     print("Good")


z = int(input("number ?"))

if z:
    print("Good")
else:
    print("bad")

#    try:
#        print(x)
#     #    print(b.__next__())
#    except StopIteration as ex:
#        print("Done")
#        break

