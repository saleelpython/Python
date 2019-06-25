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


# import module1

# # # print(module1.person)

# # for x in module1.codeNumber:
# #     if x > 10:
# #         print(f"item code [{x}] cannot be processed")
# #         continue
# #     print(f"processed items {x}")

# # c = list(filter(module1.getCodeNumber, module1.codeNumber))


# # print(c)


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

# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )

# print(colours)




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

