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