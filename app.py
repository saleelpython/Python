import module2
import csv

#region Main 
person = [
    {"_id":1, "indexID": "1001", "firstName": "Saleel", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
    {"_id":2,"indexID": "1002", "firstName": "Vrushali", "lastName": "Bagde", "canVote": "True", "canDrive": "False"}, 
    {"_id":3,"indexID": "1003", "firstName": "Sharmin", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
    {"_id":4,"indexID": "1004", "firstName": "Nitish", "lastName": "Patil", "canVote": "True", "canDrive": "True"}, 
    {"_id":5,"indexID": "1005", "firstName": "Neel", "lastName": "Save", "canVote": "False", "canDrive": "True"}, 
    {"_id":6,"indexID": "1006", "firstName": "Deep", "lastName": "Save", "canVote": "False", "canDrive": "False"}, 
    {"_id":7,"indexID": "1007", "firstName": "Ruhan", "lastName": "Bagde", "canVote": "False", "canDrive": "False"}
]

countries = ["India", "Indonesia", "Thailand", "Sri Lanka", "Comoros", "Saudi Arabia", "South Africa", "Djibouti", "France", "Malaysia", "Vietnam", "Maldives", "Oman", "Kuwait", "Eritrea", "Mozambique", "Australia", "Myanmar", "Brunei", "Mauritius", "Iran", "Bahrain", "Sudan", "Somalia", "New Zealand", "Philippines", "Cambodia", "Madagascar", "UAE", "Israel", "Kenya", "USA", "Japan", "Singapore", "Bangladesh", "Seychelles", "Qatar", "Egypt", "Tanzania", "UK", "South Korea", "Russia", "Israel", "Tajikistan", "Jordan", "Lebanon", "Panama", "Jamaica", "Namibia", "Botswana", "Fiji", "Uruguay", "Kuwait", "Denmark", "Palestine", "Mongolia", "Kosovo", "Cyprus", "Bahamas", "Marshall Islands", "Greenland", "Iceland", "Greece", "Portugal", "Belgium", "Zambia", "Zimbabwe", "Netherlands", "Syria", "Argentina", "Tanzania", "Spain", "Ukraine", "Kenya", "Uganda", "Uzbekistan", "Afghanistan", "Madagascar", "Romania", "Kazakhstan"]

def getData(l):
    for i in l:
        yield i

x = getData(countries)

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

#endregion


