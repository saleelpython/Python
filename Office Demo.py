#https://github.com/KeithGalli/Pandas-Data-Science-Tasks


func(value)             Caller      Normal argument: matched by position
func(name=value)        Caller      Keyword argument: matched by name
func(*sequence)         Caller      Pass all object in sequence as individual positional arguments
func(**dict)	        Caller      Pass all key/value pairs in dict as individual keyword arguments
def func(name)	        Function    Normal argument: matched any passed value by position or name
def func(name=value)	Function    Default argument value, if not passed in the call
def func(*name)	        Function    Matches and collects remaining positional arguments in a tuple
def func(**name)        Function    Matches and collects remaining keyword arguments in a dictionary
def func(*args, name)	Function    Arguments that must be passed by keyword only in calls


# True and non-empty things are true. Number 1 is true.
# False, None, zero, and empty things are false.

#!C:\Users\saleel\AppData\Local\Programs\Python\Python37-32\python


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.



# In Python any non-zero integer value is true; zero is false.


# Comprehensions in Python - list --[] / set -- {} and dict -- {k:v} 


# Packing and Unpacking Arguments in Python
# We use two operators * (for tuples) and ** (for dictionaries).



# List Comprehensions 
# Syntax 


# new_list = [expression(i) for i in old_list if filter(i)]


# Eg of List - []

# names = ['saleel','amit','sharmin','vrushali','saleel','sharmin','ram','laxman','anoop','sachin','suraj','amol','pankaj','neel','deep','nitish','sharmin','ruhan','bandish','supriya','sangita','suraj','vrushali']

# newNames = [n for n in names if str(n).startswith('s')]
# print(newNames)


# Eg of Set()
# newNames = {n for n in names if str(n).startswith('s') and len(n) >=7}
# print(newNames)


# s = 'This is the test by saleel'
# x = sum(set(s.count(i) for i in s if i in ['a','e','i','o','u']))
# print(x)


# dict = {i : names.count(i) for i in names}
# for i in dict:
#     print(f'{i} : {dict[i]}')



# vowels = ['a', 'e', 'i', 'o', 'u']
# s = "this is the test by saleel"
# i = {i + " " + str(s.count(i)) for i in s if i in vowels}


#------------------------------------------------------------------


# string='saleel'
# print(string[:4] if len(string) < 10 else string[0])

# l = [i for i in range(1,11) if i < 7]



# a, b, *c = 1,2,3,4,5
# print(a,b, c)

# a, b, *c, d = 1,2,3,4,5
# print(a, b, c, d)



# a, b, *c = 1,2, {"_id":"1001"}, {"_id":"1002"}, {"_id":"1003"}


# for i in range(len(c)):
#     for key, value in c[i].items():
#         print(f'{key} {value}')




# fruits = [(1, "apple"), (3, 'orange'), (4, "grapes"), (5, "mango"), (2, "kiwi")]
# a = [3,2,1,5,4]
# x = [tuple for i in a for tuple in fruits if tuple[0] == i]
# print(x)



#---------------------------------------------------------

# Generator 

# numbers = (1001,1002,1003, 1004, 1005, 1006, 1006, 1007, 1008, 1009, 1010)
# def getList(l):
#     for i in l:
#         yield i
# x = getList(numbers)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))




# def all_even():
#     n = 0
#     while True:
#         yield n
#         n += 1

# x = all_even()

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))



#---------------------------------------------------------

# countries = ["India", "Indonesia", "Thailand", "Sri Lanka", "Comoros", "Saudi Arabia", "South Africa", "Djibouti", "France", "Malaysia", "Vietnam", "Maldives", "Oman", "Kuwait", "Eritrea", "Mozambique", "Australia", "Myanmar", "Brunei", "Mauritius", "Iran", "Bahrain", "Sudan", "Somalia", "New Zealand", "Philippines", "Cambodia", "Madagascar", "UAE", "Israel", "Kenya", "USA", "Japan", "Singapore", "Bangladesh", "Seychelles", "Qatar", "Egypt", "Tanzania", "UK", "South Korea", "Russia", "Israel", "Tajikistan", "Jordan", "Lebanon", "Panama", "Jamaica", "Namibia", "Botswana", "Fiji", "Uruguay", "Kuwait", "Denmark", "Palestine", "Mongolia", "Kosovo", "Cyprus", "Bahamas", "Marshall Islands", "Greenland", "Iceland", "Greece", "Portugal", "Belgium", "Zambia", "Zimbabwe", "Netherlands", "Syria", "Argentina", "Tanzania", "Spain", "Ukraine", "Kenya", "Uganda", "Uzbekistan", "Afghanistan", "Madagascar", "Romania", "Kazakhstan"]

# fruits = ['blackberry', 'grapes', 'blueberry', 'fig', 'lemon', 'watermelon', 'apple', 'kiwi', 'lime', 'mango','blackberry']

# x = fruits.__iter__()

# while True:
#     try:
#         print(x.__next__())
#     except StopIteration:
#         print('done')
#         break



#---------------------------------------------------------

# print(['word','name','color','games'][int(input("Enter index "))])



# while (a:= int(input('continue '))) < 10:
#     print('saleel')



# fruit = ['blackberry', 'grapes', 'blueberry', 'fig', 'lemon', 'watermelon', 'apple', 'kiwi', 'lime', 'mango','blackberry']

# country = ["Afghanistan", "Italy", "India", "Japan", "United Kingdom", "Vietnam", "Russia", "Nepal", "Bangladesh"]

# capital = ["Kabul", "Rome", "New Delhi", "Tokyo", "London", "Hanoi", "Moscow", "Kathmandu", "Dhaka"]

# cities = [[1,2], [3,4], [5,6], [7,8], [9, 10], [11, 12], [13,14], [15,16], [17,18]]




# a = 5
# b = 1
# for x in range(1, a + 1):
#     b *= x
#     print(x)
# print(b)




# www ="www.google.com"
# d = dict()
# for x in www:
#    d[x] = www.count(x)
# print(d)



# string = "www.google.com"
# d = {}
# for x in string:
#     d.setdefault(x, string.count(x))
# print(d)



# www = "www.google.com"
# d = dict()
# for i in range(len(www)):
#     d.setdefault(www[i], www.count(www[i]))



# l1 = [1, 3, 5, 7, 9]
# l2 = [2, 4, 6, 8, 8, 10]

# l3=[]
# a = 0
# b = 0

# while a < len(l1) and b < len(l2) :
#    if l1[a] < l2[b]:
#       l3.append(l1[a])
#       a+=1
#    else :
#       l3.append(l2[b])
#       b+=1

# print(l3)



# poem = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star How I wonder what you are!"

# l = list()
# for i in poem:
    # x = poem.count(i), [ii for ii in poem if ii == i]
    # if x not in l:
        # l.append(x)

# for key, value in enumerate(l, start=1):
    # print(f"{value}")





# productList = set()
# z=None
# while (c := input('do you want to continue (y)es/ (n)o ')) == 'y':
#     x, x1 = (z := input('d'), len(z))
#     if x1 > 6 :
#         productList.add(z)
#     else:
#         print(f'Length of proeuct {x, x1} is less than 6')

# print(productList)





# person = [{"firstName": "Saleel", "lastName": "Bagde"}]

# def printPerson(per):
#     for key, value in per.items():
#         print(f"{key}{value}")
    




# codeNumber = [1, 56, 7, 4, 2, 4, 7, 5, 34, 67, 42, 2, 4, 5,]
# def getCodeNumber(c):
#         if c > 10:
#                 return True
#         else:
#                 return False


# names = ['saleel', 'vrushali', 'sharmin']
# number = [ 1, 4, 3]
# fn = lambda name: (x for x in zip(number, names))
# for x in fn(names):
#     print(x)



# import random

# z = ["North", "South", "East", "West"]
# deck = list(range(1, 53))

# print(random.sample(deck, 5))
# print(random.sample(deck, 5))
# print(random.sample(deck, 5))
# print(random.sample(deck, 5))





# import random
# print(random.choice(['North', 'South', 'East', 'West']))



# import module1

# # # print(module1.person)

# # for x in module1.codeNumber:
# #     if x > 10:
# #         print(f"item code [{x}] cannot be processed")
# #         continue
# #     print(f"processed items {x}")

# # c = list(filter(module1.getCodeNumber, module1.codeNumber))
# # print(c)


# l1 = [x for x in range(6)]
# l2 = ['blackberry', 'grapes', 'blueberry', 'fig', 'lemon','kiwi','mango']
# for x in zip(l1, l2):
#     print(x)





# l1 = [1, 4, 5, 3, 1, 7, 2]
# l2 = [4, 1, 6, 8, 4, 2, 8, 0]
# print([x for x in l1 if x not in l2])




# country = ["Afghanistan", "Italy", "India", "Japan", "United Kingdom", "Vietnam", "Russia", "Nepal", "Bangladesh"]
# capital = ["Kabul", "Rome", "New Delhi", "Tokyo", "London", "Hanoi", "Moscow", "Kathmandu", "Dhaka"]
# state = []

# world = {key: value for key, value in zip(country, capital)}

# for k, v in world.items():
#     print(f"{k}:{v}")




# que = ['Q' + str(x) for x in range(1, 11)]
# opt = ['a' + str(x)+")" for x in range(1, 5)]


# for q in que:
#     print(f"{q})","What is DBT?")
#     print("")
#     print("Option")
#     # print("")
#     for o in opt:
#         print(f"{o}")
    
#     print()
#     print('--------------------------')
#     print()


# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('saleel'))



# for x in range(1, 1000):
#     print(round(random.random(),5))




# ll = {}

# for i in l:
#    ll[i] = abs(i-24)
# #    print(i, abs(i-15))

# m = min(ll.values())
# print(f"----------------Key: {m}------------------")
# print()
# for key, value in ll.items():
#     # print(f"key->{key}  value->{value}")
#     if value == m:
#         print(key)
#         break




# l1 = ['sharmin', 'ruhan', 'nitish', 'saleel', 'neel', 'deep', 'gau', 'saleel']
# l2 = ('sharmin', 'ruhan', 'nitish', 'saleel', 'neel', 'deep', 'gau', 'saleel')

# for key, value in enumerate(l1,100):
#    print(f"{key} - {value}")
# print("------------------------------")
# for key, value in enumerate(l2):
#    print(f"{key} - {value}")

# def fn(**kwargs):
#    for keys, values in kwargs.items():
#       print(f"{keys} {values}")

# fn(firstName='Saleel', lastName='Bagde')


# data = {"_id":"1001", "name":"saleel", "canVote":True, "canDrive":True}

# def fn(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} {value}")
    
# fn(**data)






# person = dict(x=1, y=2, z=3)
# person1 = dict({'x':1, "y":2, "z":3})
# person2 = dict({'x':1, "y":2}, z=3)

# def fn(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} {value}')





# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )

# print(colours)






# fruits = ['apple', 'orange', 'grapes', 'mango']

# def fn(l=[]):
#     for x in l:
#         if x in fruits:
#             print("Present")
   
# fn(['grapes','grapes'])


#------------ JSON progs.. ----------------------------------


# import json

# with open ('emp.json', 'r') as fp:
#     data = json.load(fp)

# for i in range(int(input ('first')), len(data)):
#     print(f'SrNo. [{i}] - {data[i]["ename"]}')




# import json

# with open("data.json","r") as fs:
#     data = json.load(fs)
#     print(data)

# cnt = 1
# for i in data:
#     i.update({"indexID" : cnt})
#     cnt+=1
#     for key, value in i.items():
#         print(f'{key} : {value}')
#     print()
#     print('-' *48)
#     print()





#---------------------------------------------------



# import json as js

# Employee=[
#     {"ID": "1001", "firstName": "Saleel", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
#     {"ID": "1002", "firstName": "Vrushali", "lastName": "Bagde", "canVote": "True", "canDrive": "False"}, 
#     {"ID": "1003", "firstName": "Sharmin", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
#     {"ID": "1004", "firstName": "Nitish", "lastName": "Patil", "canVote": "True", "canDrive": "True"}, 
#     {"ID": "1005", "firstName": "Neel", "lastName": "Save", "canVote": "False", "canDrive": "True"}, 
#     {"ID": "1006", "firstName": "Deep", "lastName": "Save", "canVote": "False", "canDrive": "False"}, 
#     {"ID": "1007", "firstName": "Ruhan", "lastName": "Bagde", "canVote": "False", "canDrive": "False"}
# ]
# data = js.dumps(Employee)
# x = js.loads(data)
# print(x)

# ---------------------------------------------------
# import json

# with open('Superstore.json') as p:
#     data = json.load(p)

# for i in range(0, len(data)):
#     print(f"Document {i}")
#     print();
#     for key, value in data[i].items():
#         print(f"{key} : {value}")
#     print();
#     print("-----------------------------------")

# ---------------------------------------------------
# def getRegion(d):
#     if d['Region'] in "West":
#         return True
#     else:
#         return False

# r = list(filter(getRegion, data))

# for i in range(0, len(r)):
#     print(f"Document {i}")
#     print(r[i]['Row ID'])
#     print(r[i]['Order ID'])
#     print(r[i]['Order Date'])
#     print((r[i]['Region']))

#     print("-----------------------------")



# ------------------------------------------------------------


# Person = [
#     {"_id":1, "indexID": "1001", "firstName": "Saleel", "lastName": "Bagde", "canVote": True, "canDrive": True}, 
#     {"_id":2,"indexID": "1002", "firstName": "Vrushali", "lastName": "Bagde", "canVote": False, "canDrive": True}, 
#     {"_id":3,"indexID": "1003", "firstName": "Sharmin", "lastName": "Bagde", "canVote": True, "canDrive": False}  
# ]

# def fn(d):
#     return True if d["canVote"] == True else False

# x = filter(fn, Person)
# print(list(x))



# ---------------------------------------------------

# import json

# with open("Person.json") as p:
#     data = json.load(p)

# l=[]   
# for i in data:
#     l.append(int(i["ID"]))


# def findName(d):
#     if int(d["ID"]) in l: # [1001, 1002, 1005]:
#         return True
#     else:
#         return False

# p = list(filter(findName, data))

# for i in range(0, len(p)):
#     for keys, values in p[i].items():
#         print(f"{keys} {values}")
#     print("----------------------------")



# def fn(data):
  
#     for i in data:
#         yield i

# with open("emp.json", "r") as fs:
#     customer = json.load(fs)
#     data = fn(customer)

#     while (x := True if ord(input("Do you want to continue ")[0]) not in [48, 70] else False) == True:
#         try:
#             print(data.__next__())
#         except StopIteration as ex:
#             print("End of data file!")




# print(help('for'))


# def fn(a):
#     return ["Odd", "Even"][a%2==0]

# print(fn(int(input('Enter number'))))


# def g(l, h):
#     for x in range(l, h):
#         yield x




# emp = [
#         {"indexID": 1, "firstName": "Saleel", "canVote":"True", "canDrive":"False","qty":4, "rate":1000},
#         {"indexID": 2, "firstName": "Sharmin", "canVote": "True", "canDrive": "False","qty":7, "rate":475},
#         {"indexID": 3, "firstName": "Vrushali", "canVote": "True", "canDrive": "True","qty":6, "rate":500},
#         {"indexID": 4, "firstName": "Nitish", "canVote": "True", "canDrive": "True","qty":10, "rate":1200},
#         {"indexID": 5, "firstName": "Ruhan", "canVote": "True", "canDrive": "True","qty":12, "rate":750}
#     ]


# for e in emp:
#     e.update({"Total": e.get('qty') * e.get('rate')})

# for e in emp:
#     for key, value in e.items():
#         print(f"{key} - {value}")
#     print('-' * 40)



# l = [input("Products: ") for x in range(6)]

# for x in l:
#     print(f"{str.title(x)}")


# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 435, 576]
# l2 = [1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 15, 12]


# for x in range(len(l1)):
#         if l1[x] not in l2:
#                 print(l1[x])



# customer = [
#         {"id": "1001", "name": "saleel", "products": ['pen', 'nut', 'hammer', 'rubber']},
#         {"id": "1002", "name": "sharmin", "products": ['mobile', 'maggi', 'suger', 'tv']},
#         {"id": "1003", "name": "vrushali", "products": ['tea', 'coffee', 'banana', 'orange']},
#         {"id": "1004", "name": "ruhan", "products": ['bag', 'ball', 'belt', 'cycle']},
#         {"id":"1005", "name": "neel", "products": ['mobile', 'head phone']}
#         ]

# custId = input("Enter customer Id ")

# def getCustomer(l):
#         if l["id"] == custId:
#                 return True
#         else:
#                 return False

# x = list(filter(getCustomer, customer))

# for key, value in x[0].items():
#         print(f"{key}:{value}")


# fruit = ['blackberry', 'grapes', 'blueberry', 'fig', 'lemon', 'watermelon', 'apple', 'kiwi', 'lime', 'mango']
# print([f.upper() for f in fruit])




# l1 = [1, 2, 5, 1, 6, 8, 9, 4, 2, 6, 9, 4, 1, 2, 5, 3, 1, 6, 3, 7, 9, 14]

# furit = ['orange', 'kiwi', 'lime', 'apple', 'blackberry', 'watermelon']

# l2 = []

# for x in l1:
#         if x not in l2:
#                 l2.append(x)
#         else:
#                 l2.remove(x)

# print(l2)




# GUI

# r = tk.Tk() 
# r.title('Counting Seconds') 
# firstFrame = tk.Frame(r,height="400", width="400", bg='black')

# button = tk.Button(firstFrame, text='Stop', width=35, command=r.destroy, bg="Red", fg="yellow")
# button.pack(side="left")
# label1 = tk.Label(firstFrame, text="First Name", bg='blue')
# label1.pack(side="left")

# firstFrame.pack()

# r.mainloop() 



# year = 2028

# if (year % 4) == 0 or (year % 100) == 0 or (year % 400) == 0:
#     print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))



# fruits = ['banana','grapes','orange','apple','kiwi']

# def fn(f, /):
#     if f in ['banana','grapes','orange','apple','kiwi']:
#         return True
#     else:
#         return False
       
# for x in filter(fn, ['banana','grapes','orange','apple','kiwi']):
#     if (store := len(x)) > 5:
#         print(f'{x} has {store} char')
#     else:
#         print(f'{x} has {store} char')

#-----------------------------------------------------

#DRY and WET codding


# time = int(input("Enter Time "))

# def fn1(t):
#     if t >= 1 and t <= 6 :
#        print("day")
#     else:
#        print('sorry there no available driver around you!')

# def fn2(t):
#     if t >= 7 and t <= 12 :
#        print("night")
#     else:
#        print('sorry there no available driver around you!!
#        ')

# def main(a):
#     fn1(a)
#     fn2(a)

# main(time)


# -------------------------------

# import tkinter as tk

# win = tk.Tk()
# win.geometry("645x100+500+200")
# Title = tk.StringVar()
# Title.set("Infoway Technologies pvt., ltd by saleel from Python")
# win.title(Title.get())
# f1 = tk.Frame(win, width=600, height=400, bg='tomato')

# counter = tk.IntVar()

# str1 = tk.StringVar()
# str1.set("Output Window...")

# def fn(event):
#     counter.set(counter.get() + 1)
#     print("Hello Python", "Hello World", counter.get())
#     print(userName.get())
    
# def fn1(event):
#     print("<Enter>")

# userName = tk.Entry(f1, width='30')
# userName.grid(row=0, column=0)
# # userName.pack()

# btn = tk.Button(f1, text="Python", width='30')
# btn.bind("<Button-1>", fn)
# btn.bind("<Enter>", fn1)
# btn.grid(row=0, column=1)
# # btn.pack()

# lbl1 = tk.Label(f1, text=str1.get(), width='30')
# lbl1.grid(row=0, column=2)

# f1.pack(side='left')

# win.mainloop()

#---------------------------------------------------------------------

# MongoDB

# import pymongo

# client = pymongo.MongoClient(host="192.168.100.20", port= 27017)
# db = client['primaryDB']
# collection = db["emp"]

# for i in collection.find({}, {"_id":False}) :
#     for key, value in i.items():
#         print(f"{key} : {value}")
#     print()
#     print('-'*30)
#     print()




# import json
# import pymongo


# with open("person.json", 'r') as fs:
#     data = json.load(fs)

# try:
#     mongoDBClient = pymongo.MongoClient(host='192.168.100.20', port = 27017)

#     db = mongoDBClient.get_database('primaryDB')

#     # collection = db.get_collection('empq')
#     collection = db['per']
#     print(f'"db" : "{db.name}" - "collection" : "{collection.name}"')
#     print('-' * 42)

#     for i in data:
#         collection.insert_one(i)
       

# except pymongo.errors.DuplicateKeyError as ex:
#     # print(list(ex.))
#     print(f'Error Code : {ex.code} \n\nMessage : {ex.args}')

# except pymongo.errors.CollectionInvalid as ex:
#     print(f'pymongo.erro {ex}')

# finally:
#     print()
#     print()
#     print()
#     print(f'Done')





#------------------------------------------------------------------------------

#Oracle connection


# pip install cx-Oracle
# import cx_Oracle

# con = cx_Oracle.connect('c##saleel/saleel@orcl')

# cursor = con.cursor() 

# x = cursor.execute("select * from emp")

# print(list(x))

#---------------------------------------------------------------------------------

# import cx_Oracle
# try:
#     con = cx_Oracle.connect('c##saleel/saleel@orcl')
#     cursor = con.cursor() 
#     cursor.execute("insert all into dept values(1,1,1,1) into dept values(2,1,1,1) select * from dual")
#     con.commit()

# except cx_Oracle.DatabaseError as ex:
#      print("There is a problem with Oracle", ex)

# finally:
#     print('Connection closed!')
#     cursor.close()
#     con.close()

#------------------------------------------------------------

#region CSV

#Region,	Country, ItemType, SalesChannel, OrderPriority, OrderDate, OrderID, ShipDate, UnitsSold, UnitPrice, UnitCost, TotalRevenue', TotalCost, TotalProfit
# l = list()
# with open ("SalesRecords2.csv" ,'r') as fs:
#     data = csv.reader(fs)
  
#     for i in data:
#         l.append({"Region":i[0], "Country":i[1], "ItemType":i[2], "SalesChannel":i[3], "OrderPriority":i[4], "OrderDate":i[5], "OrderID":int(i[6]), "ShipDate":i[7], "UnitsSold": int(i[8]), "UnitPrice":float( i[9]), "UnitCost": float(i[10]), "TotalRevenue":float(i[11]), "TotalCost":float(i[12]), "TotalProfit": float(i[13])})

# for i in range(len(l)):
#     print(l[i])
#     print('-' * 55)
#endregion


#------------------------------------------------------------


#region Pandas 
#names=["Region","Country","ItemType","SalesChannel","OrderPriority","OrderDate","OrderID","ShipDate","UnitsSold","UnitPrice","UnitCost","TotalRevenue","TotalCost","TotalProfit"], header=None

# df = pandas.read_csv("weather.csv", names=["season","temperature","humidity","wind_speed","wind_gust","dailyRain","monthlyRain","yearlyRain","uv_0_11","date"], header=None )

# pandas.set_option('display.max_rows', None)
# pandas.set_option('display.max_columns', None)
# pandas.set_option('display.max_colwidth', 60)
# pandas.set_option('display.width', None)
# pandas.set_option("display.colheader_justify","left")


# print(df[["season","temperature","humidity"]])
# # print(df)

# df = pandas.DataFrame(person)

# print(df[['indexID', 'firstName', 'canVote']])




#-----------------------------------------------------------------------------------

# If condition in Pandas
# df.loc[df['column name'] condition, 'new column name'] = 'value if condition is met'


# pandas.set_option('display.max_rows', None)
# pandas.set_option('display.max_columns', None)
# pandas.set_option('display.max_colwidth',20)
# pandas.set_option('display.width', None)


# df = pandas.read_csv("police.csv",names=["stop_date", "stop_time","county_name", "driver_gender","driver_age_raw", "driver_age", "driver_race", "violation_raw", "violation", "search_conducted", "search_type", "stop_outcome", "is_arrested", "stop_duration", "drugs_related_stop"], header=None, nrows=1175)

# with open("weather.csv" , 'r') as fs:
    # df = pandas.read_csv("weather.csv", names=["season","temperature","humidity","wind_speed","wind_gust","dailyRain","monthlyRain","yearlyRain","uv_0_11","date"], header=None, nrows = None)

# df = pandas.read_csv("movie.csv", names=["_id", "relese", "color", "director","critic","duration","director_facebook","actor_3_facebook","actor_2_name",	"actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords",	"movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes","production houses"], header=None )

# df = pandas.read_csv("all_data.csv", names=["Order ID", "Product", "Quantity Ordered", "Price Each" , "Order Date" , "Purchase Address"], header=None)


# # df.fillna('Not Available', inplace=True)

# df["color"].fillna("No Data", inplace=True)

# df.fillna(value={"color": "Color", "critic": 450, "director":"Not Available", "director_facebook":"Not Available"}, inplace=True)

# # print(df.columns)

# print(df["duration"].max())

# print(df["duration"].min())

# df.sort_values("duration", inplace=True)

df.rename(columns={"Day" : "New Day", "Month":"New Month"}, inplace=True)
print( df.columns )

df.rename( columns={ "Customer_Age" : "Customer Age", "Age_Group" : "AgeGroup", "Customer_Gender" : "Customer Gender",
                     "Product_Category" : "Product Category", "Order_Quantity" : "Order Quantity",
                     "Unit_Cost" : "Unit Cost", "Unit_Price" : "Unit Price" }, inplace=True )


print( len( df.columns ) )

print ( df[["New Day", "New Month", "Year"]] )

print(df.describe())
print(df[["Day", "Year"]].describe())

print(df.info())
print(df[["Day", "Year"]].info())



# print(df[["color", "director","movie_title","critic","duration","director_facebook","actor_3_facebook","actor_2_name"]][df["duration"] == 150])

# print(df[["color", "director","movie_title","critic","duration","director_facebook","actor_3_facebook","actor_2_name"]][df["duration"] >= 450])

# print(df[["color", "director","movie_title","critic","duration","director_facebook","actor_3_facebook","actor_2_name"]][df["duration"] == df["duration"].max()])

# print(df[["color", "director","movie_title","critic","duration","director_facebook","actor_3_facebook","actor_2_name"]][df["duration"] == df["duration"].min()])

# print(df[["movieColorType", "movie_title", "language", "country", "director", "critic", "duration"]].to_string(index=False))

# print(df[["movieColorType" , "director", "critic", "duration", "movie_title", "actor_2_name","plot_keywords","imdb_score"]][(df['duration'] == 100) & (df["movieColorType"] == 'Black and White')])

# print(df[["movieColorType","director","duration"]] [df["duration"] == 100].count())

# print(df[["movieColorType" , "director", "critic", "duration", "movie_title", "actor_2_name","plot_keywords","imdb_score","content_rating"]] [((df["content_rating"] =='PG-13') | (df["content_rating"] == 'U/A')) & (df["duration"] == 10_0)])

# print(df[["movieColorType" , "director", "critic", "duration", "movie_title", "actor_2_name","plot_keywords","imdb_score","content_rating"]][df["content_rating"].isin(["PG-13", "U/A"])])


# print(df[["movieColorType","movie_title", "genres", "director", "critic", "duration", "language","country","content_rating"]] [(df["duration"] ==100) & (df["language"] == 'Hindi') & (df["genres"].str.contains("Drama"))])

# df.insert(1,"country", "IN")

# df["cards"] = "Master"
# df.index= ["Index - " + str(i) for i in range(df["_id"].count())]

# print(df.iloc[0])


# If condition in Pandas

# df.loc[df['ename'] == 'Sara', 'name_match'] = 'Match'
# df.loc[df['ename'] != 'Sara', 'name_match'] = 'Not Match'
# print(df[['ename', "name_match"]])


print( df[["_id", "release", "color", "director", "critic", "duration", "language", "country", "budget", "title_year",
           "production houses", "Week1", "week2", "week3", "week4", "isActive"]].loc[0 :1] )


# print()
# print()

# print(df.director)


#endregion


#region EMP
# emp = [ 
# {"indexID":1,"empid":1020,"ename":"king","address": {"building": "1007", "location": [-73.856077, 40.848447], "street": "Morris Park Ave", "zipcode": "10462"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["blue","black"], "favouriteFruit": [],"cards": [],"aadhar" :"MJAsXaaO5H", "job":"president","mgr":"","hiredate":{"$date":"1981-11-17T00:00:0000Z"},"sal":5000,"comm":"","deptno":10},
# {"indexID":2,"empid":1021,"ename":"smith","address": {"building": "469", "location": [-73.961704, 40.662942], "street": "Flatbush Avenue", "zipcode": "11225"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["red", "cyan", "gray"], "favouriteFruit": ["grapes", "Orange"],"aadhar" :"aYpI9qEzpe","job":"manager","mgr":1020,"hiredate":{"$date":"1981-05-01T00:00:0000Z"},"sal":3400,"comm":"","deptno":10},
# {"indexID":3,"empid":1022,"ename":"james","address": {"building": "351", "location": [-73.98513559999999, 40.7676919], "street": "West   57 Street", "zipcode": "10019"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["red","blue","green","yellow"], "favouriteFruit": ["Indian Fig"],"aadhar" :"Eo4fFSlzko","job":"manager","mgr":1020,"hiredate":{"$date":"1981-07-09T00:00:0000Z"},"sal":4700,"comm":"","deptno":20},
# {"indexID":4,"empid":1023,"ename":"jack","address": {"building": "2780", "location": [-73.98241999999999, 40.579505], "street": "Stillwell Avenue", "zipcode": "11224"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Air Force Blue","Apple Green"], "favouriteFruit": ["Orange"],"aadhar" :"AqTts79GMf","job":"accountant","mgr":1022,"hiredate":{"$date":"1981-04-02T00:00:0000Z"},"sal":2700,"comm":"","deptno":30},
# {"indexID":5,"empid":1023,"ename":"scott","address": {"building": "97-22", "location": [-73.8601152, 40.7311739], "street": "63 Road", "zipcode": "11374"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Ash Grey"], "favouriteFruit": [],"aadhar" :"BbZSlE5Shr","job":"salesman","mgr":1023,"hiredate":{"$date":"1981-09-28T00:00:0000Z"},"sal":2500,"comm":350,"deptno":30},
# {"indexID":6,"empid":1024,"ename":"martin","address": {"building": "8825", "location": [-73.8803827, 40.7643124], "street": "Astoria Boulevard", "zipcode": "11369"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Banana Yellow"], "favouriteFruit": [],"aadhar" :"V4oEJ5YO60","job":"salesman","mgr":1023,"hiredate":{"$date":"1981-02-20T00:00:0000Z"},"sal":2900,"comm":735,"deptno":30},
# {"indexID":7,"empid":1025,"ename":"crow","address": {"building": "2206", "location": [-74.1377286, 40.6119572], "street": "Victory Boulevard", "zipcode": "10314"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Apple Green","Ash Grey"], "favouriteFruit": [],"aadhar" :"aLbMmPcpqM","job":"salesman","mgr":1023,"hiredate":{"$date":"1981-09-08T00:00:0000Z"},"sal":3200,"comm":"","deptno":20},
# {"indexID":8,"empid":1026,"ename":"blake","address": {"building": "7114", "location": [-73.9068506, 40.6199034], "street": "Avenue U", "zipcode": "11234"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Brass","Bright Green"], "favouriteFruit": [],"aadhar" :"DqMpSf5zTR","job":"clerk","mgr":1024,"hiredate":{"$date":"1981-12-03T00:00:0000Z"},"sal":1200,"comm":"","deptno":30},
# {"indexID":9,"empid":1027,"ename":"richards","address": {"building": "6409", "location": [-740528899999999, 40.628886], "street": "11 Avenue", "zipcode": "11219"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Charcoal","Cherry"], "favouriteFruit": [],"aadhar" :"T1xG2CSxMV","job":"clerk","mgr":1024,"hiredate":{"$date":"1981-02-22T00:00:0000Z"},"sal":1500,"comm":"","deptno":10},
# {"indexID":10,"empid":1028,"ename":"peter","address": {"building": "1839", "location": [-73.9482609, 40.6408271], "street": "Nostrand Avenue", "zipcode": "11226"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Brown"], "favouriteFruit": ["banana","Jackfruit"],"aadhar" :"X3ZmceNzLf","job":"analyst","mgr":1025,"hiredate":{"$date":"1981-12-03T00:00:0000Z"},"sal":3500,"comm":"","deptno":30},
# {"indexID":11,"empid":1029,"ename":"bob","address": {"building": "2300", "location": [-73.8786113, 40.8502883], "street": "Southern Boulevard", "zipcode": "10460"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Copper"], "favouriteFruit": [],"aadhar" :"Xv7ck7WIgp","job":"manager","mgr":1020,"hiredate":{"$date":"1980-12-17T00:00:0000Z"},"sal":4900,"comm":"","deptno":30},
# {"indexID":12,"empid":1030,"ename":"saleel","address": {"building": "7715", "location": [-73.9973325, 40.61174889999999], "street": "18 Avenue", "zipcode": "11214"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Coral"], "favouriteFruit": ["Dates","Orange"],"aadhar" :"K8ZqWrIOwB","job":"programmer","mgr":1020,"hiredate":{"$date":"1982-12-09T00:00:0000Z"},"sal":2900,"comm":"","deptno":10},
# {"indexID":13,"empid":1031,"ename":"sharmin","address": {"building": "1269", "location": [-73.871194, 40.6730975], "street": "Sutter Avenue", "zipcode": "11208"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Cream"], "favouriteFruit": ["Indian Fig"],"aadhar" :"QhmI8yPiAU","job":"programmer","mgr":1020,"hiredate":{"$date":"1983-01-12T00:00:0000Z"},"sal":4999,"comm":"","deptno":40},
# {"indexID":14,"empid":1032,"ename":"vrushali","address": {"building": "1", "location": [-73.96926909999999, 40.7685235], "street": "East   66 Street", "zipcode": "10065"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Iceberg"], "favouriteFruit": ["Orange","Papaya", "Kiwi"],"aadhar" :"FG8u8ktwAG","job":"analyst","mgr":1030,"hiredate":{"$date":"1982-02-23T00:00:0000Z"},"sal":4999,"comm":"","deptno":20},
# {"indexID":15,"empid":1033,"ename":"vasant","address": {"building": "705", "location": [-73.9653967, 40.6064339], "street": "Kings Highway", "zipcode": "11223"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Bright Green"], "favouriteFruit": [],"aadhar" :"YiPEcNOjLT","job":"salesman","mgr":1029,"hiredate":{"$date":"1982-02-24T00:00:0000Z"},"sal":2200,"comm":0,"deptno":40},
# {"indexID":16,"empid":1034,"ename":"vasu","address": {"building": "203", "location": [-73.97822040000001, 40.6435254], "street": "Church Avenue", "zipcode": "11218"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": ["Dates"],"aadhar" :"9YG0G20F4O","job":"salesman","mgr":1029,"hiredate":{"$date":"1980-02-14T00:00:0000Z"},"sal":2200,"comm":250,"deptno":40},
# {"indexID":17,"empid":1035,"ename":"rahul","address": {"building": "265-15", "location": [-73.7032601, 40.7386417], "street": "Hillside Avenue", "zipcode": "11004"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Indian Red"], "favouriteFruit": ["Lychee","Indian Fig"],"aadhar" :"XxwwGjp2ZE","job":"clerk","mgr":1029,"hiredate":{"$date":"1981-12-31T00:00:0000Z"},"sal":1200,"comm":"","deptno":40},
# {"indexID":18,"empid":1036,"ename":"raju","address": {"building": "6909", "location": [-74259567, 40.6353674], "street": "3 Avenue", "zipcode": "11209"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Indian Yellow"], "favouriteFruit": ["Crab apples"],"aadhar" :"CjODdMBJxh","job":"administrator","mgr":1031,"hiredate":{"$date":"1983-06-15T00:00:0000Z"},"sal":3400,"comm":"","deptno":50},
# {"indexID":19,"empid":1037,"ename":"ramu","address": {"building": "522", "location": [-73.95171, 40.767461], "street": "East   74 Street", "zipcode": "10021"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Lemon"], "favouriteFruit": ["Jackfruit","banana", "Apple"],"aadhar" :"0MrIAAQ5a7","job":"clerk","mgr":1031,"hiredate":{"$date":"1983-07-12T00:00:0000Z"},"sal":1400,"comm":"","deptno":50},
# {"indexID":20,"empid":1038,"ename":"neel","address": {"building": "284", "location": [-73.9829239, 40.6580753], "street": "Prospect Park West", "zipcode": "11215"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Apple Green"], "favouriteFruit": [],"aadhar" :"E8A7IH0hwJ","job":"administrator","mgr":1030,"hiredate":{"$date":"1983-03-14T00:00:0000Z"},"sal":4200,"comm":"","deptno":10},
# {"indexID":21,"empid":1039,"ename":"saleel","address": {"building": "129-08", "location": [-73.839297, 40.78147], "street": "20 Avenue", "zipcode": "11356"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Cherry","Charcoal"], "favouriteFruit": [],"aadhar" :"cvuzqy0Ias","job":"analyst","mgr":1022,"hiredate":{"$date":"1982-12-09T00:00:0000Z"},"sal":3700,"comm":"","deptno":50},
# {"indexID":22,"empid":1040,"ename":"amit","address": {"building": "759", "location": [-73.9925306, 40.7309346], "street": "Broadway", "zipcode": "10003"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Indian Red"], "favouriteFruit": ["Crab apples"],"aadhar" :"XzvRNmJzVQ","job":"administrator","mgr":1029,"hiredate":{"$date":"1982-12-08T00:00:0000Z"},"sal":3500,"comm":"","deptno":50,"phone":[8.5088422e+07,{"$numberLong":"9822884228"}]},
# {"indexID":23,"empid":1041,"ename":"dinesh","address": {"building": "3406", "location": [-73.94024739999999, 40.7623288], "street": "10 Street", "zipcode": "11106"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Air Force Blue"], "favouriteFruit": [],"aadhar" :"GTt0uDmKx5","job":"programmer","mgr":1021,"hiredate":{"$date":"1982-12-09T00:00:0000Z"},"sal":3500,"comm":"","deptno":50,"phone":[8.5088422e+07,{"$numberLong":"9822884228"}],"skills":{"language":["C++","JAVA"],"web":["php","java","jquery"]}},
# {"indexID":24,"empid":1040,"ename":"amit","address": {"building": "502", "location": [-73.976112, 40.786714], "street": "Amsterdam Avenue", "zipcode": "10024"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Orange"], "favouriteFruit": [],"aadhar" :"b7o2kAqTk2","job":"administrator","mgr":1029,"hiredate":{"$date":"1981-11-03T00:00:0000Z"},"sal":3500,"comm":"","deptno":50,"phone":["9850884228","9822884228"]},
# {"indexID":25,"empid":1041,"ename":"dinesh","address": {"building": "730", "location": [-73.96805719999999, 40.7925587], "street": "Columbus Avenue", "zipcode": "10025"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Navy Blue"], "favouriteFruit": [],"aadhar" :"GMRgu5DyDy","job":"programmer","mgr":1021,"hiredate":{"$date":"1981-11-04T00:00:0000Z"},"sal":3500,"comm":"","deptno":50,"phone":["020-25420200",{"$numberLong":"9822336644"}],"skills":{"language":["C++","JAVA"],"web":["php","java","jquery"]}},
# {"indexID":26,"empid":1042,"ename":"rudra","address": {"building": "18", "location": [-73.996984, 40.72589], "street": "West Houston Street", "zipcode": "10012"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Lime"], "favouriteFruit": ["Indian Fig"],"aadhar" :"ijOoAiRLZK","job":"programmer","mgr":1021,"hiredate":{"$date":"1981-11-04T00:00:0000Z"},"sal":2400,"comm":"","deptno":50,"phone":"020-25420212","skills":{"web":["php","java","jquery"],"database":["oracle","ms-sql server","mongodb"]}},
# {"indexID":27,"empid":1043,"ename":"pankaj","address": {"building": "531", "location": [-73.9634876, 40.6940001], "street": "Myrtle Avenue", "zipcode": "11205"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["White"], "favouriteFruit": ["Peach"],"aadhar" :"0oxAOliq9p","job":"programmer","mgr":1023,"hiredate":{"$date":"1980-02-17T00:00:0000Z"},"sal":3600,"comm":"","deptno":40,"phone":"022-2548345","skills":{"language":".NET","database":"ms-sql server"}},
# {"indexID":28,"empid":1044,"ename":"anoop","address": {"building": "103-05", "location": [-73.8642349, 40.75356], "street": "37 Avenue", "zipcode": "11368"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Navy Blue"], "favouriteFruit": [],"aadhar" :"FmsbfXnBr8","job":"programmer","mgr":1029,"hiredate":{"$date":"1980-02-17T00:00:0000Z"},"sal":2300,"comm":1200,"deptno":50,"phone":"022-2548345","skills":{"language":[".NET","java"],"database":"oracle","web":["json","jquery","javascript"]}},
# {"indexID":29,"empid":1045,"ename":"nitish","address": {"building": "60", "location": [-74085357, 40.70620539999999], "street": "Wall Street", "zipcode": "10005"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Coral","Cream"], "favouriteFruit": [],"aadhar" :"4WpLg6Ly4H","job":"programmer","mgr":1039,"hiredate":{"$date":"1980-03-14T00:00:0000Z"},"sal":1300,"comm":1200,"deptno":50,"phone":"022-2548345","skills":{"language":[".NET","java"],"database":{"rdbms":["oracle","db2"],"nosql":["mongodb","hive"]},"web":["json","jquery","javascript","php"]}},
# {"indexID":30,"empid":1046,"ename":"neel","address": {"building": "195", "location": [-73.9246028, 40.6522396], "street": "East   56 Street", "zipcode": "11203"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Orange"], "favouriteFruit": [],"aadhar" :"nX46yWpJQ8","job":"programmer","mgr":1039,"hiredate":{"$date":"1980-03-14T00:00:0000Z"},"sal":1800,"comm":1400,"deptno":50,"phone":"022-2534565","skills":{"language":"ruby","database":{"rdbms":["oracle","db2"],"nosql":["mongodb","hive","hbase"]}}},
# {"indexID":31,"empid":1047,"ename":"arjun","address": {"building": "107", "location": [-740920839999999, 40.7132925], "street": "Church Street", "zipcode": "10007"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Sky Blue"], "favouriteFruit": ["Lychee"],"aadhar" :"G0LWSnlHcx","job":"auditor","mgr":1020,"hiredate":{"$date":"1984-05-05T00:00:0000Z"},"sal":3200,"comm":"","hra":1500,"da":1200,"deptno":20},
# {"indexID":32,"empid":1048,"ename":"amol","address": {"building": "1006", "location": [-73.84856870000002, 40.8903781], "street": "East 233 Street", "zipcode": "10466"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Snow White"], "favouriteFruit": ["Orange"],"aadhar" :"d9KznYQs6L","job":"auditor","mgr":1047,"hiredate":{"$date":"1984-05-06T00:00:0000Z"},"sal":3800,"comm":"","hra":1000,"da":900,"deptno":20},
# {"indexID":33,"empid":1049,"ename":"sangita","address": {"building": "56", "location": [-73.991495, 40.692273], "street": "Court Street", "zipcode": "11201"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["White"], "favouriteFruit": ["Papaya"],"aadhar" :"q90io2xPtx","job":"auditor","mgr":1040,"hiredate":{"$date":"1984-03-30T00:00:0000Z"},"sal":3100,"comm":"","hra":1000,"da":1500,"deptno":20},
# {"indexID":34,"empid":1050,"ename":"gita","address": {"building": "7615", "location": [-74228449, 40.6281815], "street": "5 Avenue", "zipcode": "11209"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Indian Red"], "favouriteFruit": ["Kiwi"],"aadhar" :"GIr294gRmn","job":"writer","language":["english","hindi"],"mgr":1049,"hiredate":{"$date":"1984-03-29T00:00:0000Z"},"sal":2150,"comm":750,"hra":1300,"da":1700,"deptno":40},
# {"indexID":35,"empid":1051,"ename":"sita","address": {"building": "120", "location": [-73.9998042, 40.7251256], "street": "Prince Street", "zipcode": "10012"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Snow White"], "favouriteFruit": ["Guava"],"aadhar" :"2HecAK1UgG","job":"writer","language":["english","hindi","marathi"],"mgr":1049,"hiredate":{"$date":"1984-03-30T00:00:0000Z"},"sal":3755,"comm":750,"hra":1100,"da":1100,"deptno":40},
# {"indexID":36,"empid":2001,"ename":"pinky","address": {"building": "1236", "location": [-73.8893654, 40.81376179999999], "street": "238 Spofford Ave", "zipcode": "10474"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": ["banana","Jackfruit"],"aadhar" :"GdHilITn3L","job":"Computer Programmer","mgr":1039,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":3500,"comm":"","deptno":10},
# {"indexID":37,"empid":2002,"ename":"priti","address": {"building": "625", "location": [-73.990494, 40.7569545], "street": "8 Avenue", "zipcode": "10018"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Violet"], "favouriteFruit": [],"aadhar" :"Z3O3VTesma","job":"Computer Programmer","mgr":1037,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":5500,"comm":"","deptno":20},
# {"indexID":38,"empid":2003,"ename":"supriya","address": {"building": "1069", "location": [-73.902463, 40.694924], "street": "Wyckoff Avenue", "zipcode": "11385"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Snow White"], "favouriteFruit": [],"aadhar" :"iZ71YezboW","job":"Computer Programmer","mgr":2001,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":3500,"comm":"","deptno":30},
# {"indexID":39,"empid":2004,"ename":"sangu","address": {"building": "405", "location": [-73.97534999999999, 40.7516269], "street": "Lexington Avenue", "zipcode": "10174"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Apple Green"], "favouriteFruit": ["Passion Fruit"],"aadhar" :"mOyCK3OiCG","job":"Computer Programmer","mgr":2002,"hiredate":{"$date":"1980-07-17T00:00:0000Z"},"sal":6000,"comm":"","deptno":10},
# {"indexID":40,"empid":2005,"ename":"laxman","address": {"building": "2491", "location": [-74.1459332, 40.6103714], "street": "Victory Boulevard", "zipcode": "10314"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": [],"aadhar" :"EKoCSlHrs3","job":"Computer Programmer","mgr":2001,"hiredate":{"$date":"1980-11-17T00:00:0000Z"},"sal":6500,"comm":"","deptno":20},
# {"indexID":41,"empid":2006,"ename":"rahsmi","address": {"building": "7905", "location": [-73.8740217, 40.7135015], "street": "Metropolitan Avenue", "zipcode": "11379"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Orange"], "favouriteFruit": ["Peach"],"aadhar" :"cEfjBb0T3v","job":"Computer Programmer","mgr":2002,"hiredate":{"$date":"1982-05-17T00:00:0000Z"},"sal":5600,"comm":"","deptno":30},
# {"indexID":42,"empid":2007,"ename":"raj","address": {"building": "87-69", "location": [-73.8309503, 40.7001121], "street": "Lefferts Boulevard", "zipcode": "11418"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Dark Orange"], "favouriteFruit": ["Papaya"],"aadhar" :"rrVtn0Vpmg","job":"Computer Programmer","mgr":1039,"hiredate":{"$date":"1981-08-17T00:00:0000Z"},"sal":7000,"comm":"","deptno":40},
# {"indexID":43,"empid":2008,"ename":"roselin","address": {"building": "1418", "location": [-73.95685019999999, 40.7753401], "street": "Third Avenue", "zipcode": "10028"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["White"], "favouriteFruit": ["watermelon","mango"],"aadhar" :"AL1yiIPCuR","job":"Computer Programmer","mgr":2005,"hiredate":{"$date":"1983-02-17T00:00:0000Z"},"sal":800,"comm":"","deptno":30},
# {"indexID":44,"empid":2009,"ename":"janhavi","address": {"building": "464", "location": [-73.9791458, 40.744328], "street": "3 Avenue", "zipcode": "10016"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Violet"], "favouriteFruit": ["Papaya"],"aadhar" :"tZZtzeBih2","job":"Computer Programmer","mgr":2002,"hiredate":{"$date":"1983-08-17T00:00:0000Z"},"sal":4700,"comm":"","deptno":40},
# {"indexID":44,"empid":2010,"ename":"jasu","address": {"building": "437", "location": [-73.975393, 40.757365], "street": "Madison Avenue", "zipcode": "10022"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Lawn Green"], "favouriteFruit": ["Fig","apple"],"aadhar" :"fkehFzIADu","job":"Computer Programmer","mgr":2007,"hiredate":{"$date":"1983-04-17T00:00:0000Z"},"sal":5800,"comm":"","deptno":40},
# {"indexID":46,"empid":2011,"ename":"snehal","address": {"building": "1031", "location": [-73.9075537, 40.6438684], "street": "East   92 Street", "zipcode": "11236"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": ["apple"],"aadhar" :"GdHilI123L","job":"WEB Programmer","mgr":1039,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":2500,"comm":"","deptno":10},
# {"indexID":47,"empid":2012,"ename":"rupal","address": {"building": "1111", "location": [-74796436, 40.59878339999999], "street": "Hylan Boulevard", "zipcode": "10305"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Violet"], "favouriteFruit": ["grapes"],"aadhar" :"Z3O3VTesMJ","job":"WEB Programmer","mgr":1037,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":6500,"comm":"","deptno":20},
# {"indexID":48,"empid":2013,"ename":"bandish","address": {"building": "976", "location": [-73.92701509999999, 40.6620192], "street": "Rutland Road", "zipcode": "11212"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Snow White"], "favouriteFruit": ["mango"],"aadhar" :"iZ71Y34boW","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":7000,"comm":"","deptno":30},
# {"indexID":49,"empid":2014,"ename":"madhavi","address": {"building": "148", "location": [-73.9806854, 40.7778589], "street": "West   72 Street", "zipcode": "10023"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Apple Green"], "favouriteFruit": ["mango"],"aadhar" :"mOyCK53iCG","job":"WEB Programmer","mgr":2002,"hiredate":{"$date":"1980-07-17T00:00:0000Z"},"sal":6900,"comm":"","deptno":10},
# {"indexID":50,"empid":2015,"ename":"ram","address": {"building": "364", "location": [-73.96084119999999, 40.8014307], "street": "West  110 Street", "zipcode": "10025"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": ["cherry", "grapes"],"aadhar" :"EKoCSKHrs3","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1980-11-17T00:00:0000Z"},"sal":6200,"comm":"","deptno":20},
# {"indexID":51,"empid":2016,"ename":"aditi","address": {"building": "1423", "location": [-73.9615132, 40.6253268], "street": "Avenue J", "zipcode": "11230"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Orange"], "favouriteFruit": ["lime","Guava"],"aadhar" :"cEf54b0T3v","job":"WEB Programmer","mgr":2002,"hiredate":{"$date":"1982-05-17T00:00:0000Z"},"sal":5700,"comm":"","deptno":30},
# {"indexID":52,"empid":2017,"ename":"neeraj","address": {"building": "0", "location": [-84.2040813, 9.9986585], "street": "Guardia Airport Parking", "zipcode": "11371"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Dark Orange"], "favouriteFruit": ["pineapple"],"aadhar" :"rrVtn40Vmg","job":"WEB Programmer","mgr":1039,"hiredate":{"$date":"1981-08-17T00:00:0000Z"},"sal":7700,"comm":"","deptno":40},
# {"indexID":53,"empid":2018,"ename":"meera","address": {"building": "73", "location": [-74.1178949, 40.5734906], "street": "New Dorp Plaza", "zipcode": "10306"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["White"], "favouriteFruit": ["watermelon"],"aadhar" :"AL1yi77CuR","job":"WEB Programmer","mgr":2005,"hiredate":{"$date":"1983-02-17T00:00:0000Z"},"sal":950,"comm":"","deptno":30},
# {"indexID":54,"empid":2019,"ename":"zara","address": {"building": "277", "location": [-73.8941893, 40.8634684], "street": "East Kingsbridge Road", "zipcode": "10458"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Violet"], "favouriteFruit": ["Dragon Fruit"],"aadhar" :"tZZtzeBi72","job":"WEB Programmer","mgr":2002,"hiredate":{"$date":"1983-08-17T00:00:0000Z"},"sal":3700,"comm":"","deptno":40},
# {"indexID":55,"empid":2020,"ename":"tanvi","address": {"building": "203", "location": [-74.15235919999999, 40.5563756], "street": "Giffords Lane", "zipcode": "10308"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Lawn Green"], "favouriteFruit": ["Avocado"],"aadhar" :"fke43zIADu","job":"WEB Programmer","mgr":2007,"hiredate":{"$date":"1983-04-17T00:00:0000Z"},"sal":5700,"comm":"","deptno":40},
# {"indexID":56,"empid":2021,"ename":"Emma","address": {"building": "2031", "location": [-78.15235919456999, 47.5568756], "street": "Giffords Lane", "zipcode": "11309"},"isActive": True,"gender": "female", "canVote": True, "canDrive":True, "favouriteColor": ["Lawn Green", "Sky Blue"], "favouriteFruit": ["Avocado","Grapes","Orance"], "aadhar" :"fke43zIAZX","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1982-04-17T00:00:0000Z"},"sal":7700,"comm":"","deptno":10},
# {"indexID":57,"empid":2022,"ename":"Emma","address": {"building": "2031", "location": [-78.15235919456999, 47.5568756], "street": "Keesey Street", "zipcode": "11310"},"isActive": False,"gender": "female", "canVote": False, "canDrive":True, "favouriteColor": ["Lawn Green", "Sky Blue"], "favouriteFruit": ["Avocado","Grapes","Orance"], "aadhar" :"fke43zIAZz","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1982-08-17T00:00:0000Z"}, "sal":7000,"comm":"","deptno":10},
# {"indexID":58,"empid":2023,"ename":"Olivia","address": {"building": "031", "location": [-78.15231429456999, 42.5560956], "street": "Hazel Grove", "zipcode": "133038"},"isActive": True,"gender": "female", "canVote": False, "canDrive":True, "favouriteColor": ["Lawn Green", "Sky Blue"], "favouriteFruit": ["Banana","Grapes","Orance"], "aadhar" :"fke43HIAZX","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1981-06-17T00:00:0000Z"}, "sal":9000,"comm":"","deptno":10},
# {"indexID":59,"empid":2024,"ename":"Mia","address": {"building": "032", "location": [-78.15235919456999, 43.5578756], "street": "Kidd Cottages", "zipcode": "33038"},"isActive": False,"gender": "female", "canVote": False, "canDrive":True, "favouriteColor": ["Light Pink", "Light Blue"], "favouriteFruit": ["Orance"], "aadhar" :"fKe43zIAZX","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1983-04-17T00:00:0000Z"}, "sal":9500,"comm":"","deptno":10},
# {"indexID":60,"empid":2025,"ename":"Emily","address": {"building": "7036", "location": [-78.15299819456999, 40.5568756], "street": "Adams Row", "zipcode": "15310"},"isActive": False, "gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Yellow"], "favouriteFruit": ["Grapes"], "aadhar" :"fke73zIAZz","job":"WEB Programmer","mgr":2004,"hiredate":{"$date":"1981-04-19T00:00:0000Z"}, "sal":7600,"comm":"","deptno":40},
# {"indexID":61,"empid":2026,"ename":"Sophia","address": {"building": "7036", "location": [-78.15299819456999, 40.5568756], "street": "Adams Row", "zipcode": "15310"},"isActive": False, "gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Gray"], "favouriteFruit": ["Orange"], "aadhar" :"fke73JzIAz","job":"Designer","mgr":2007,"hiredate":{"$date":"1983-09-11T00:00:0000Z"}, "sal":6600,"comm":1200,"deptno":40},
# {"indexID":62,"empid":2027,"ename":"Queen","address": {"building": "7036", "location": [-78.15299819456999, 40.5568756], "street": "Adams Row", "zipcode": "15310"},"isActive": False, "gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Cyan"], "favouriteFruit": ["Grapes"], "aadhar" :"fkR73JzIAz","job":"Designer","mgr":2007,"hiredate":{"$date":"1983-09-11T00:00:0000Z"}, "sal":7500,"comm":1000,"deptno":40},
# {"indexID":63,"empid":2028,"ename":"Sara","address": {"building": "7036", "location": [-78.15299819456999, 40.5568756], "street": "Adams Row", "zipcode": "15310"},"isActive": False, "gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Cyan"], "favouriteFruit": ["Grapes"], "aadhar" :"fkR78JzIAz","job":"Designer","mgr":2007,"hiredate":{"$date":"1981-09-11T00:00:0000Z"}, "sal":4500,"comm":"","deptno":40},
# {"indexID":64,"empid":2029,"ename":"Sara","address": {"building": "7036", "location": [-72.15299456999, 46.5568756], "street": "Supreme Court", "zipcode": "15372"},"isActive": True, "gender": "female", "canVote": True, "canDrive":True, "favouriteColor": ["Cyan"], "favouriteFruit": ["kiwi"], "aadhar" :"fkR78JzIAz","job":"Designer","mgr":2007,"hiredate":{"$date":"1981-09-17T00:00:0000Z"}, "sal":4500,"comm":5000,"deptno":30},
# {"indexID":65,"empid":2030,"ename":"aarav","address": {"building": "1007", "location": [-73.856077, 40.848447], "street": "Morris Park Ave", "zipcode": "10462"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["blue","black"], "favouriteFruit": [],"cards": [],"aadhar" :"MJAsXaaO5H", "job":"president","mgr":"","hiredate":{"$date":"1981-11-17T00:00:0000Z"},"sal":5000,"comm":"","deptno":10},
# {"indexID":66,"empid":2031,"ename":"vivaan","address": {"building": "469", "location": [-73.961704, 40.662942], "street": "Flatbush Avenue", "zipcode": "11225"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["red", "cyan", "gray"], "favouriteFruit": ["grapes", "Orange"],"aadhar" :"aYpI9qEzpe","job":"manager","mgr":1020,"hiredate":{"$date":"1981-05-01T00:00:0000Z"},"sal":3400,"comm":"","deptno":10},
# {"indexID":67,"empid":2032,"ename":"aditya","address": {"building": "351", "location": [-73.98513559999999, 40.7676919], "street": "West   57 Street", "zipcode": "10019"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["red","blue","green","yellow"], "favouriteFruit": ["Indian Fig"],"aadhar" :"Eo4fFSlzko","job":"manager","mgr":1020,"hiredate":{"$date":"1981-07-09T00:00:0000Z"},"sal":4700,"comm":"","deptno":20},
# {"indexID":68,"empid":2033,"ename":"arjun","address": {"building": "2780", "location": [-73.98241999999999, 40.579505], "street": "Stillwell Avenue", "zipcode": "11224"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Air Force Blue","Apple Green"], "favouriteFruit": ["Orange"],"aadhar" :"AqTts79GMf","job":"accountant","mgr":1022,"hiredate":{"$date":"1981-04-02T00:00:0000Z"},"sal":2700,"comm":"","deptno":30},
# {"indexID":69,"empid":2034,"ename":"reyansh","address": {"building": "97-22", "location": [-73.8601152, 40.7311739], "street": "63 Road", "zipcode": "11374"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Ash Grey"], "favouriteFruit": [],"aadhar" :"BbZSlE5Shr","job":"salesman","mgr":1023,"hiredate":{"$date":"1981-09-28T00:00:0000Z"},"sal":2500,"comm":350,"deptno":30},
# {"indexID":70,"empid":2035,"ename":"sai","address": {"building": "8825", "location": [-73.8803827, 40.7643124], "street": "Astoria Boulevard", "zipcode": "11369"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Banana Yellow"], "favouriteFruit": [],"aadhar" :"V4oEJ5YO60","job":"salesman","mgr":1023,"hiredate":{"$date":"1981-02-20T00:00:0000Z"},"sal":2900,"comm":735,"deptno":30},
# {"indexID":71,"empid":2036,"ename":"ayaan","address": {"building": "2206", "location": [-74.1377286, 40.6119572], "street": "Victory Boulevard", "zipcode": "10314"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Apple Green","Ash Grey"], "favouriteFruit": [],"aadhar" :"aLbMmPcpqM","job":"salesman","mgr":1023,"hiredate":{"$date":"1981-09-08T00:00:0000Z"},"sal":3200,"comm":"","deptno":20},
# {"indexID":72,"empid":2037,"ename":"shaurya","address": {"building": "7114", "location": [-73.9068506, 40.6199034], "street": "Avenue U", "zipcode": "11234"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Brass","Bright Green"], "favouriteFruit": [],"aadhar" :"DqMpSf5zTR","job":"clerk","mgr":1024,"hiredate":{"$date":"1981-12-03T00:00:0000Z"},"sal":1200,"comm":"","deptno":30},
# {"indexID":73,"empid":2038,"ename":"dhruv","address": {"building": "6409", "location": [-740528899999999, 40.628886], "street": "11 Avenue", "zipcode": "11219"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Charcoal","Cherry"], "favouriteFruit": [],"aadhar" :"T1xG2CSxMV","job":"clerk","mgr":1024,"hiredate":{"$date":"1981-02-22T00:00:0000Z"},"sal":1500,"comm":"","deptno":10},
# {"indexID":74,"empid":2039,"ename":"krishna","address": {"building": "1839", "location": [-73.9482609, 40.6408271], "street": "Nostrand Avenue", "zipcode": "11226"},"isActive": True,"gender": "male","canVote": True, "canDrive":False,"favouriteColor": ["Brown"], "favouriteFruit": ["banana","Jackfruit"],"aadhar" :"X3ZmceNzLf","job":"analyst","mgr":1025,"hiredate":{"$date":"1981-12-03T00:00:0000Z"},"sal":3500,"comm":"","deptno":30},
# {"indexID":75,"empid":2040,"ename":"krish","address": {"building": "2300", "location": [-73.8786113, 40.8502883], "street": "Southern Boulevard", "zipcode": "10460"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Copper"], "favouriteFruit": [],"aadhar" :"Xv7ck7WIgp","job":"manager","mgr":1020,"hiredate":{"$date":"1980-12-17T00:00:0000Z"},"sal":4900,"comm":"","deptno":30},
# {"indexID":76,"empid":2041,"ename":"ishaan","address": {"building": "7715", "location": [-73.9973325, 40.61174889999999], "street": "18 Avenue", "zipcode": "11214"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Coral"], "favouriteFruit": ["Dates","Orange"],"aadhar" :"K8ZqWrIOwB","job":"programmer","mgr":1020,"hiredate":{"$date":"1982-12-09T00:00:0000Z"},"sal":2900,"comm":"","deptno":10},
# {"indexID":77,"empid":2042,"ename":"kabir","address": {"building": "1269", "location": [-73.871194, 40.6730975], "street": "Sutter Avenue", "zipcode": "11208"},"isActive": False,"gender": "female","canVote": True, "canDrive":False,"favouriteColor": ["Cream"], "favouriteFruit": ["Indian Fig"],"aadhar" :"QhmI8yPiAU","job":"programmer","mgr":1020,"hiredate":{"$date":"1983-01-12T00:00:0000Z"},"sal":4999,"comm":"","deptno":40},
# {"indexID":78,"empid":2043,"ename":"rudra","address": {"building": "1", "location": [-73.96926909999999, 40.7685235], "street": "East   66 Street", "zipcode": "10065"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Iceberg"], "favouriteFruit": ["Orange","Papaya", "Kiwi"],"aadhar" :"FG8u8ktwAG","job":"analyst","mgr":1030,"hiredate":{"$date":"1982-02-23T00:00:0000Z"},"sal":4999,"comm":"","deptno":20},
# {"indexID":79,"empid":2044,"ename":"om","address": {"building": "705", "location": [-73.9653967, 40.6064339], "street": "Kings Highway", "zipcode": "11223"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Bright Green"], "favouriteFruit": [],"aadhar" :"YiPEcNOjLT","job":"salesman","mgr":1029,"hiredate":{"$date":"1982-02-24T00:00:0000Z"},"sal":2200,"comm":0,"deptno":40},
# {"indexID":80,"empid":2045,"ename":"chetan","address": {"building": "203", "location": [-73.97822040000001, 40.6435254], "street": "Church Avenue", "zipcode": "11218"},"isActive": False,"gender": "male","canVote": True, "canDrive":False,"favouriteColor": ["India Green"], "favouriteFruit": ["Dates"],"aadhar" :"9YG0G20F4O","job":"salesman","mgr":1029,"hiredate":{"$date":"1980-02-14T00:00:0000Z"},"sal":2200,"comm":250,"deptno":40},
# {"indexID":81,"empid":2046,"ename":"rahul","address": {"building": "265-15", "location": [-73.7032601, 40.7386417], "street": "Hillside Avenue", "zipcode": "11004"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Indian Red"], "favouriteFruit": ["Lychee","Indian Fig"],"aadhar" :"XxwwGjp2ZE","job":"clerk","mgr":1029,"hiredate":{"$date":"1981-12-31T00:00:0000Z"},"sal":1200,"comm":"","deptno":40},
# {"indexID":82,"empid":2047,"ename":"raju","address": {"building": "6909", "location": [-74259567, 40.6353674], "street": "3 Avenue", "zipcode": "11209"},"isActive": True,"gender": "male","canVote": True, "canDrive":False, "favouriteColor": ["Indian Yellow"], "favouriteFruit": ["Crab apples"],"aadhar" :"CjODdMBJxh","job":"administrator","mgr":1031,"hiredate":{"$date":"1983-06-15T00:00:0000Z"},"sal":3400,"comm":"","deptno":50},
# {"indexID":83,"empid":2048,"ename":"manish","address": {"building": "522", "location": [-73.95171, 40.767461], "street": "East   74 Street", "zipcode": "10021"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Lemon"], "favouriteFruit": ["Jackfruit","banana", "Apple"],"aadhar" :"0MrIAAQ5a7","job":"clerk","mgr":1031,"hiredate":{"$date":"1983-07-12T00:00:0000Z"},"sal":1400,"comm":"","deptno":50},
# {"indexID":84,"empid":2049,"ename":"manoj","address": {"building": "284", "location": [-73.9829239, 40.6580753], "street": "Prospect Park West", "zipcode": "11215"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Apple Green"], "favouriteFruit": [],"aadhar" :"E8A7IH0hwJ","job":"administrator","mgr":1030,"hiredate":{"$date":"1983-03-14T00:00:0000Z"},"sal":4200,"comm":"","deptno":10},
# {"indexID":85,"empid":2050,"ename":"mohan","address": {"building": "129-08", "location": [-73.839297, 40.78147], "street": "20 Avenue", "zipcode": "11356"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Cherry","Charcoal"], "favouriteFruit": [],"aadhar" :"cvuzqy0Ias","job":"analyst","mgr":1022,"hiredate":{"$date":"1982-12-09T00:00:0000Z"},"sal":3700,"comm":"","deptno":50},
# {"indexID":86,"empid":2051,"ename":"rajesh","address": {"building": "759", "location": [-73.9925306, 40.7309346], "street": "Broadway", "zipcode": "10003"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Indian Red"], "favouriteFruit": ["Crab apples"],"aadhar" :"XzvRNmJzVQ","job":"administrator","mgr":1029,"hiredate":{"$date":"1982-12-08T00:00:0000Z"},"sal":3500,"comm":"","deptno":50,"phone":[8.5088422e+07,{"$numberLong":"9822884228"}]},
# {"indexID":87,"empid":2052,"ename":"sanjay","address": {"building": "3406", "location": [-73.94024739999999, 40.7623288], "street": "10 Street", "zipcode": "11106"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Air Force Blue"], "favouriteFruit": [],"aadhar" :"GTt0uDmKx5","job":"programmer","mgr":1021,"hiredate":{"$date":"1982-12-09T00:00:0000Z"},"sal":3500,"comm":"","deptno":50,"phone":[8.5088422e+07,{"$numberLong":"9822884228"}],"skills":{"language":["C++","JAVA"],"web":["php","java","jquery"]}},
# {"indexID":88,"empid":2053,"ename":"rohit","address": {"building": "502", "location": [-73.976112, 40.786714], "street": "Amsterdam Avenue", "zipcode": "10024"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Orange"], "favouriteFruit": [],"aadhar" :"b7o2kAqTk2","job":"administrator","mgr":1029,"hiredate":{"$date":"1981-11-03T00:00:0000Z"},"sal":3500,"comm":"","deptno":50,"phone":["9850884228","9822884228"]},
# {"indexID":89,"empid":2054,"ename":"vijay","address": {"building": "730", "location": [-73.96805719999999, 40.7925587], "street": "Columbus Avenue", "zipcode": "10025"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Navy Blue"], "favouriteFruit": [],"aadhar" :"GMRgu5DyDy","job":"programmer","mgr":1021,"hiredate":{"$date":"1981-11-04T00:00:0000Z"},"sal":3500,"comm":"","deptno":50,"phone":["020-25420200",{"$numberLong":"9822336644"}],"skills":{"language":["C++","JAVA"],"web":["php","java","jquery"]}},
# {"indexID":90,"empid":2055,"ename":"vinod","address": {"building": "18", "location": [-73.996984, 40.72589], "street": "West Houston Street", "zipcode": "10012"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Lime"], "favouriteFruit": ["Indian Fig"],"aadhar" :"ijOoAiRLZK","job":"programmer","mgr":1021,"hiredate":{"$date":"1981-11-04T00:00:0000Z"},"sal":2400,"comm":"","deptno":50,"phone":"020-25420212","skills":{"web":["php","java","jquery"],"database":["oracle","ms-sql server","mongodb"]}},
# {"indexID":91,"empid":2056,"ename":"kamal","address": {"building": "531", "location": [-73.9634876, 40.6940001], "street": "Myrtle Avenue", "zipcode": "11205"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["White"], "favouriteFruit": ["Peach"],"aadhar" :"0oxAOliq9p","job":"programmer","mgr":1023,"hiredate":{"$date":"1980-02-17T00:00:0000Z"},"sal":3600,"comm":"","deptno":40,"phone":"022-2548345","skills":{"language":".NET","database":"ms-sql server"}},
# {"indexID":92,"empid":2057,"ename":"navin","address": {"building": "103-05", "location": [-73.8642349, 40.75356], "street": "37 Avenue", "zipcode": "11368"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Navy Blue"], "favouriteFruit": [],"aadhar" :"FmsbfXnBr8","job":"programmer","mgr":1029,"hiredate":{"$date":"1980-02-17T00:00:0000Z"},"sal":2300,"comm":1200,"deptno":50,"phone":"022-2548345","skills":{"language":[".NET","java"],"database":"oracle","web":["json","jquery","javascript"]}},
# {"indexID":93,"empid":2058,"ename":"nitish","address": {"building": "60", "location": [-74085357, 40.70620539999999], "street": "Wall Street", "zipcode": "10005"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Coral","Cream"], "favouriteFruit": [],"aadhar" :"4WpLg6Ly4H","job":"programmer","mgr":1039,"hiredate":{"$date":"1980-03-14T00:00:0000Z"},"sal":1300,"comm":1200,"deptno":50,"phone":"022-2548345","skills":{"language":[".NET","java"],"database":{"rdbms":["oracle","db2"],"nosql":["mongodb","hive"]},"web":["json","jquery","javascript","php"]}},
# {"indexID":94,"empid":2059,"ename":"neel","address": {"building": "195", "location": [-73.9246028, 40.6522396], "street": "East   56 Street", "zipcode": "11203"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Orange"], "favouriteFruit": [],"aadhar" :"nX46yWpJQ8","job":"programmer","mgr":1039,"hiredate":{"$date":"1980-03-14T00:00:0000Z"},"sal":1800,"comm":1400,"deptno":50,"phone":"022-2534565","skills":{"language":"ruby","database":{"rdbms":["oracle","db2"],"nosql":["mongodb","hive","hbase"]}}},
# {"indexID":95,"empid":2060,"ename":"arjun","address": {"building": "107", "location": [-740920839999999, 40.7132925], "street": "Church Street", "zipcode": "10007"},"isActive": True,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Sky Blue"], "favouriteFruit": ["Lychee"],"aadhar" :"G0LWSnlHcx","job":"auditor","mgr":1020,"hiredate":{"$date":"1984-05-05T00:00:0000Z"},"sal":3200,"comm":"","hra":1500,"da":1200,"deptno":20},
# {"indexID":96,"empid":2061,"ename":"dev","address": {"building": "1006", "location": [-73.84856870000002, 40.8903781], "street": "East 233 Street", "zipcode": "10466"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Snow White"], "favouriteFruit": ["Orange"],"aadhar" :"d9KznYQs6L","job":"auditor","mgr":1047,"hiredate":{"$date":"1984-05-06T00:00:0000Z"},"sal":3800,"comm":"","hra":1000,"da":900,"deptno":20},
# {"indexID":97,"empid":2062,"ename":"sangita","address": {"building": "56", "location": [-73.991495, 40.692273], "street": "Court Street", "zipcode": "11201"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["White"], "favouriteFruit": ["Papaya"],"aadhar" :"q90io2xPtx","job":"auditor","mgr":1040,"hiredate":{"$date":"1984-03-30T00:00:0000Z"},"sal":3100,"comm":"","hra":1000,"da":1500,"deptno":20},
# {"indexID":98,"empid":2063,"ename":"gita","address": {"building": "7615", "location": [-74228449, 40.6281815], "street": "5 Avenue", "zipcode": "11209"},"isActive": True,"gender": "female","canVote": True, "canDrive":False,"favouriteColor": ["Indian Red"], "favouriteFruit": ["Kiwi"],"aadhar" :"GIr294gRmn","job":"writer","language":["english","hindi"],"mgr":1049,"hiredate":{"$date":"1984-03-29T00:00:0000Z"},"sal":2150,"comm":750,"hra":1300,"da":1700,"deptno":40},
# {"indexID":99,"empid":2064,"ename":"neil","address": {"building": "120", "location": [-73.9998042, 40.7251256], "street": "Prince Street", "zipcode": "10012"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Snow White"], "favouriteFruit": ["Guava"],"aadhar" :"2HecAK1UgG","job":"writer","language":["english","hindi","marathi"],"mgr":1049,"hiredate":{"$date":"1984-03-30T00:00:0000Z"},"sal":3755,"comm":750,"hra":1100,"da":1100,"deptno":40},
# {"indexID":100,"empid":2065,"ename":"pinky","address": {"building": "1236", "location": [-73.8893654, 40.81376179999999], "street": "238 Spofford Ave", "zipcode": "10474"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": ["banana","Jackfruit"],"aadhar" :"GdHilITn3L","job":"Computer Programmer","mgr":1039,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":3500,"comm":"","deptno":10},
# {"indexID":101,"empid":2066,"ename":"harsh","address": {"building": "625", "location": [-73.990494, 40.7569545], "street": "8 Avenue", "zipcode": "10018"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Violet"], "favouriteFruit": [],"aadhar" :"Z3O3VTesma","job":"Computer Programmer","mgr":1037,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":5500,"comm":"","deptno":20},
# {"indexID":102,"empid":2067,"ename":"supriya","address": {"building": "1069", "location": [-73.902463, 40.694924], "street": "Wyckoff Avenue", "zipcode": "11385"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Snow White"], "favouriteFruit": [],"aadhar" :"iZ71YezboW","job":"Computer Programmer","mgr":2001,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":3500,"comm":"","deptno":30},
# {"indexID":103,"empid":2068,"ename":"sangu","address": {"building": "405", "location": [-73.97534999999999, 40.7516269], "street": "Lexington Avenue", "zipcode": "10174"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Apple Green"], "favouriteFruit": ["Passion Fruit"],"aadhar" :"mOyCK3OiCG","job":"Computer Programmer","mgr":2002,"hiredate":{"$date":"1980-07-17T00:00:0000Z"},"sal":6000,"comm":"","deptno":10},
# {"indexID":104,"empid":2069,"ename":"laxman","address": {"building": "2491", "location": [-74.1459332, 40.6103714], "street": "Victory Boulevard", "zipcode": "10314"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": [],"aadhar" :"EKoCSlHrs3","job":"Computer Programmer","mgr":2001,"hiredate":{"$date":"1980-11-17T00:00:0000Z"},"sal":6500,"comm":"","deptno":20},
# {"indexID":105,"empid":2070,"ename":"rahsmi","address": {"building": "7905", "location": [-73.8740217, 40.7135015], "street": "Metropolitan Avenue", "zipcode": "11379"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Orange"], "favouriteFruit": ["Peach"],"aadhar" :"cEfjBb0T3v","job":"Computer Programmer","mgr":2002,"hiredate":{"$date":"1982-05-17T00:00:0000Z"},"sal":5600,"comm":"","deptno":30},
# {"indexID":106,"empid":2071,"ename":"raj","address": {"building": "87-69", "location": [-73.8309503, 40.7001121], "street": "Lefferts Boulevard", "zipcode": "11418"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Dark Orange"], "favouriteFruit": ["Papaya"],"aadhar" :"rrVtn0Vpmg","job":"Computer Programmer","mgr":1039,"hiredate":{"$date":"1981-08-17T00:00:0000Z"},"sal":7000,"comm":"","deptno":40},
# {"indexID":107,"empid":2072,"ename":"roselin","address": {"building": "1418", "location": [-73.95685019999999, 40.7753401], "street": "Third Avenue", "zipcode": "10028"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["White"], "favouriteFruit": ["watermelon","mango"],"aadhar" :"AL1yiIPCuR","job":"Computer Programmer","mgr":2005,"hiredate":{"$date":"1983-02-17T00:00:0000Z"},"sal":800,"comm":"","deptno":30},
# {"indexID":108,"empid":2073,"ename":"janhavi","address": {"building": "464", "location": [-73.9791458, 40.744328], "street": "3 Avenue", "zipcode": "10016"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Violet"], "favouriteFruit": ["Papaya"],"aadhar" :"tZZtzeBih2","job":"Computer Programmer","mgr":2002,"hiredate":{"$date":"1983-08-17T00:00:0000Z"},"sal":4700,"comm":"","deptno":40},
# {"indexID":109,"empid":2074,"ename":"jasu","address": {"building": "437", "location": [-73.975393, 40.757365], "street": "Madison Avenue", "zipcode": "10022"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Lawn Green"], "favouriteFruit": ["Fig","apple"],"aadhar" :"fkehFzIADu","job":"Computer Programmer","mgr":2007,"hiredate":{"$date":"1983-04-17T00:00:0000Z"},"sal":5800,"comm":"","deptno":40},
# {"indexID":110,"empid":2075,"ename":"snehal","address": {"building": "1031", "location": [-73.9075537, 40.6438684], "street": "East   92 Street", "zipcode": "11236"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": ["apple"],"aadhar" :"GdHilI123L","job":"WEB Programmer","mgr":1039,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":2500,"comm":"","deptno":10},
# {"indexID":111,"empid":2076,"ename":"rupal","address": {"building": "1111", "location": [-74796436, 40.59878339999999], "street": "Hylan Boulevard", "zipcode": "10305"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Violet"], "favouriteFruit": ["grapes"],"aadhar" :"Z3O3VTesMJ","job":"WEB Programmer","mgr":1037,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":6500,"comm":"","deptno":20},
# {"indexID":112,"empid":2077,"ename":"bandish","address": {"building": "976", "location": [-73.92701509999999, 40.6620192], "street": "Rutland Road", "zipcode": "11212"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Snow White"], "favouriteFruit": ["mango"],"aadhar" :"iZ71Y34boW","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1983-07-17T00:00:0000Z"},"sal":7000,"comm":"","deptno":30},
# {"indexID":113,"empid":2078,"ename":"madhavi","address": {"building": "148", "location": [-73.9806854, 40.7778589], "street": "West   72 Street", "zipcode": "10023"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Apple Green"], "favouriteFruit": ["mango"],"aadhar" :"mOyCK53iCG","job":"WEB Programmer","mgr":2002,"hiredate":{"$date":"1980-07-17T00:00:0000Z"},"sal":6900,"comm":"","deptno":10},
# {"indexID":114,"empid":2079,"ename":"ram","address": {"building": "364", "location": [-73.96084119999999, 40.8014307], "street": "West  110 Street", "zipcode": "10025"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["India Green"], "favouriteFruit": ["cherry", "grapes"],"aadhar" :"EKoCSKHrs3","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1980-11-17T00:00:0000Z"},"sal":6200,"comm":"","deptno":20},
# {"indexID":115,"empid":2080,"ename":"aditi","address": {"building": "1423", "location": [-73.9615132, 40.6253268], "street": "Avenue J", "zipcode": "11230"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Orange"], "favouriteFruit": ["lime","Guava"],"aadhar" :"cEf54b0T3v","job":"WEB Programmer","mgr":2002,"hiredate":{"$date":"1982-05-17T00:00:0000Z"},"sal":5700,"comm":"","deptno":30},
# {"indexID":116,"empid":2081,"ename":"neeraj","address": {"building": "0", "location": [-84.2040813, 9.9986585], "street": "Guardia Airport Parking", "zipcode": "11371"},"isActive": False,"gender": "male","canVote": True, "canDrive":True,"favouriteColor": ["Dark Orange"], "favouriteFruit": ["pineapple"],"aadhar" :"rrVtn40Vmg","job":"WEB Programmer","mgr":1039,"hiredate":{"$date":"1981-08-17T00:00:0000Z"},"sal":7700,"comm":"","deptno":40},
# {"indexID":117,"empid":2082,"ename":"meera","address": {"building": "73", "location": [-74.1178949, 40.5734906], "street": "New Dorp Plaza", "zipcode": "10306"},"isActive": True,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["White"], "favouriteFruit": ["watermelon"],"aadhar" :"AL1yi77CuR","job":"WEB Programmer","mgr":2005,"hiredate":{"$date":"1983-02-17T00:00:0000Z"},"sal":950,"comm":"","deptno":30},
# {"indexID":118,"empid":2083,"ename":"zara","address": {"building": "277", "location": [-73.8941893, 40.8634684], "street": "East Kingsbridge Road", "zipcode": "10458"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Violet"], "favouriteFruit": ["Dragon Fruit"],"aadhar" :"tZZtzeBi72","job":"WEB Programmer","mgr":2002,"hiredate":{"$date":"1983-08-17T00:00:0000Z"},"sal":3700,"comm":"","deptno":40},
# {"indexID":119,"empid":2084,"ename":"tanvi","address": {"building": "203", "location": [-74.15235919999999, 40.5563756], "street": "Giffords Lane", "zipcode": "10308"},"isActive": False,"gender": "female","canVote": True, "canDrive":True,"favouriteColor": ["Lawn Green"], "favouriteFruit": ["Avocado"],"aadhar" :"fke43zIADu","job":"WEB Programmer","mgr":2007,"hiredate":{"$date":"1983-04-17T00:00:0000Z"},"sal":5700,"comm":"","deptno":40},
# {"indexID":120,"empid":2085,"ename":"Emma","address": {"building": "2031", "location": [-78.15235919456999, 47.5568756], "street": "Giffords Lane", "zipcode": "11309"},"isActive": True,"gender": "female", "canVote": True, "canDrive":True, "favouriteColor": ["Lawn Green", "Sky Blue"], "favouriteFruit": ["Avocado","Grapes","Orance"], "aadhar" :"fke43zIAZX","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1982-04-17T00:00:0000Z"},"sal":7700,"comm":"","deptno":10},
# {"indexID":121,"empid":2086,"ename":"Emma","address": {"building": "2031", "location": [-78.15235919456999, 47.5568756], "street": "Keesey Street", "zipcode": "11310"},"isActive": False,"gender": "female", "canVote": False, "canDrive":True, "favouriteColor": ["Lawn Green", "Sky Blue"], "favouriteFruit": ["Avocado","Grapes","Orance"], "aadhar" :"fke43zIAZz","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1982-08-17T00:00:0000Z"}, "sal":7000,"comm":"","deptno":10},
# {"indexID":122,"empid":2087,"ename":"Olivia","address": {"building": "031", "location": [-78.15231429456999, 42.5560956], "street": "Hazel Grove", "zipcode": "133038"},"isActive": True,"gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Lawn Green", "Sky Blue"], "favouriteFruit": ["Banana","Grapes","Orance"], "aadhar" :"fke43HIAZX","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1981-06-17T00:00:0000Z"}, "sal":9000,"comm":"","deptno":10},
# {"indexID":123,"empid":2088,"ename":"Mia","address": {"building": "032", "location": [-78.15235919456999, 43.5578756], "street": "Kidd Cottages", "zipcode": "33038"},"isActive": False,"gender": "female", "canVote": False, "canDrive":True, "favouriteColor": ["Light Pink", "Light Blue"], "favouriteFruit": ["Orance"], "aadhar" :"fKe43zIAZX","job":"WEB Programmer","mgr":2001,"hiredate":{"$date":"1983-04-17T00:00:0000Z"}, "sal":9500,"comm":"","deptno":10},
# {"indexID":124,"empid":2089,"ename":"Emily","address": {"building": "7036", "location": [-78.15299819456999, 40.5568756], "street": "Adams Row", "zipcode": "15310"},"isActive": False, "gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Yellow"], "favouriteFruit": ["Grapes"], "aadhar" :"fke73zIAZz","job":"WEB Programmer","mgr":2004,"hiredate":{"$date":"1981-04-19T00:00:0000Z"}, "sal":7600,"comm":"","deptno":40},
# {"indexID":125,"empid":2090,"ename":"Sophia","address": {"building": "7036", "location": [-78.15299819456999, 40.5568756], "street": "Adams Row", "zipcode": "15310"},"isActive": False, "gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Gray"], "favouriteFruit": ["Orange"], "aadhar" :"fke73JzIAz","job":"Designer","mgr":2007,"hiredate":{"$date":"1983-09-11T00:00:0000Z"}, "sal":6600,"comm":1200,"deptno":40},
# {"indexID":126,"empid":2091,"ename":"Queen","address": {"building": "7036", "location": [-78.15299819456999, 40.5568756], "street": "Adams Row", "zipcode": "15310"},"isActive": False, "gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Cyan"], "favouriteFruit": ["Grapes"], "aadhar" :"fk344JzIAz","job":"Designer","mgr":2007,"hiredate":{"$date":"1983-09-11T00:00:0000Z"}, "sal":7500,"comm":1000,"deptno":40},
# {"indexID":127,"empid":2092,"ename":"Sara","address": {"building": "7036", "location": [-78.15299819456999, 40.5568756], "street": "Adams Row", "zipcode": "15310"},"isActive": False, "gender": "female", "canVote": False, "canDrive":False, "favouriteColor": ["Cyan"], "favouriteFruit": ["Grapes"], "aadhar" :"fkR78JzIAz","job":"Designer","mgr":2007,"hiredate":{"$date":"1981-09-11T00:00:0000Z"}, "sal":4500,"comm":"","deptno":40},
# {"indexID":128,"empid":2093,"ename":"Sara","address": {"building": "7036", "location": [-72.15299456999, 46.5568756], "street": "Supreme Court", "zipcode": "15372"},"isActive": True, "gender": "female", "canVote": True, "canDrive":True, "favouriteColor": ["Cyan"], "favouriteFruit": ["kiwi"], "aadhar" :"fkR78JzIAz","job":"Designer","mgr":2007,"hiredate":{"$date":"1981-09-17T00:00:0000Z"}, "sal":4500,"comm":5000,"deptno":30}
# ]
# df = pandas.DataFrame(emp, columns=["indexID","empid","ename","address"])

# for i in df["address"]:
#     for key, value in i.items():
#         if key == "location":
#             print(f"{key} {value}")


#endregion EMP


#-------------------------------------------------------------------------------------------


# code_dict = {'..-': 'U', '--..--': ', ', '....-': '4', '.....': '5',
# '-...': 'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q',
# '--..': 'Z', '.--': 'W', '-..-.': '/', '..---': '2',
# '.-': 'A', '..': 'I', '-.-.': 'C', '..-.': 'F',
# '---': 'O', '-.--': 'Y', '-': 'T', '.': 'E',
# '.-..': 'L', '...': 'S', '-.--.-': ')',
# '..--..': '?', '.----': '1', '-----': '0',
# '-.-': 'K', '-..': 'D', '----.': '9',
# '-....': '6', '.---': 'J', '.--.': 'P',
# '.-.-.-': '.', '-.--.': '(', '--': 'M',
# '-.': 'N', '....': 'H', '---..': '8',
# '...-': 'V', '--...': '7',
# '--.': 'G', '...--': '3', '-....-': '-'}

# string = "SALEEL"

# # for key, value in code_dict.items():
# #     print (f'{key}   {value}')

# x = ""

# for i in string:
#     for key, value in code_dict.items():
#         if i == value :
#             x = x  + key + " "

# print(x)


#--------------------------------
# import random
# import string

# alpha = [i for i in string.ascii_letters]
# code=[]

# o1, o2, o3, o4, o5, o6 = [".", "-"], ["_", "."], [".", "-"], [".", "-"], ["_", "."], [".", "-"]

# while True:
#     x = random.choice(o1)+random.choice(o2)+random.choice(o3)+random.choice(o4)+random.choice(o5)+random.choice(o6)
#     if x not in code :
#         code.append(x)

#     if code.__len__() > 51:
#         break

# code1 = {}

# for key, value in zip(alpha, code):
#     print(f'{key}    {value}')
#     code1[key] = value

# s = "SALEEL"

# print()
# print("-" * 50)
# print()
# for key, value in code1.items():
#     for i in s:
#         if i in key:
#             print(i + value)



#-----------------------------------------------------------------------------------------------------------

"""
author : saleel
db: Redis
language: python
command : program to create multiple keys in Redis using python DICT()
"""

# <editor-fold desc="all module imports">
import redis
import pandas
import string
import json

# </editor-fold>

client = redis.Redis( host='127.0.0.1', port="6379", db=2 )
client.flushdb()

d = dict( { "_id" : "1001", "firstName" : "saleel", "isActive" : 1 } )
print( d )
client.hset( "person", mapping=d )
#
x = None


def fn(d) -> object :

    for i in d :
        yield i


with open( file="countries.json", mode="r" ) as fs :
    data1 = json.load( fp=fs )
    x = filter( fn, data1 )
    while ( c := input("Do you want to continue? ") in ['Y', 'y', '1'] ) :
        print()
        print("-" * 45)
        for key, value in x.__next__().items():
            print(f"{key=} {value=}")
        print("-" * 45)

#-----------------------------------------------------------------------------------------------------------

"""
author : saleel
db: Redis
function: map
language: python
"""

# <editor-fold desc="all module imports">
import redis
import pandas
import string
import random
import json


# </editor-fold>

def fn(l) -> object :
    yield l


otp = [(i, random.randint( 2789, 4839 )) for i in range( 1, 2 )]

x = map( fn, otp )

while (c := input( "Do you eant to continue? " )) in ['y', 'Y'] :
    try :
        for i in x.__next__() :
            print( i )
    except StopIteration :
        print( StopIteration.value )
        break
#-----------------------------------------------------------------------------------------------------------
