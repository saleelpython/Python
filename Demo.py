# True and non-empty things are true. Number 1 is true.
# False, None, zero, and empty things are false.

#!C:\Users\saleel\AppData\Local\Programs\Python\Python37-32\python


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# Comprehensions in Python


# Packing and Unpacking Arguments in Python
# We use two operators * (for tuples) and ** (for dictionaries).



# List Comprehensions

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
#     # print(f"Key->{key}  value->{value}")
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

