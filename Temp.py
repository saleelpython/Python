# # print(f"{mobiles[1]['type']}")
# names = ['saleel', 'vrushali', 'sharmin', 'bandish', 'neel', 'nitish', 'deep', 'ruhan', 'sangita', 'supriya', 'gau', 'kaushal', 'natasha']


# mobiles = [{"type":"moto", "os":"android"},
# {"type": "apple", "os": "ios"},
# {"type": "nokia", "os": "ios"},
# {"type": "mi", "os": "android"}]

# def getNames(n):
#     print(n['type'])
#     # if (n[0:2] == 'sh'):
#     #     return True
#     # else:
#     #     return False
    


# nm = list(filter(getNames, mobiles))

# # print(nm)





# person = {"firstName":"saleel", "lastName":"bagde", "age":"50"}

# trainings = { "course1":{"title":"Python Training Course for Beginners", 
#                          "location":"Frankfurt", 
#                          "trainer":"Steve G. Snake"},
#               "course2":{"title":"Intermediate Python Training",
#                          "location":"Berlin",
#                          "trainer":"Ella M. Charming"},
#               "course3":{"title":"Python Text Processing Course",
#                          "location":"München",
#                          "trainer":"Monica A. Snowdon"}
#               }
    
# for key, value in trainings.items():
#     for k, v in trainings[key].items():
#         print(f"{k}:{v}")
#     print("-----------------------")



#     employees = [
#     {"city" :"Pune", "emp" : [ {"indexID": 1, "firstName": "Saleel", "canVote":"True", "canDrive":"False"},
#                                {"indexID": 2, "firstName": "Sharmin", "canVote": "True", "canDrive": "False"},
#                                {"indexID": 3, "firstName": "Vrushali", "canVote": "True", "canDrive": "True"},
#                                {"indexID": 4, "firstName": "Nitish", "canVote": "True", "canDrive": "True"},
#                                {"indexID": 5, "firstName": "Ruhan", "canVote": "True", "canDrive": "True"}
#                             ]
#     },
#     {"city" :"Baroda", "emp" : [ {"indexID": 1, "firstName": "Bhuru", "canVote": "True", "canDrive": "False"},
#                                  {"indexID": 2, "firstName": "Bhavi", "canVote": "True", "canDrive": "False"},
#                                  {"indexID": 3, "firstName": "Pinky", "canVote": "True", "canDrive": "True"},
#                                  {"indexID": 4, "firstName": "Monika", "canVote": "True", "canDrive": "True"},
#                                  {"indexID": 5, "firstName": "Sangita", "canVote": "True", "canDrive": "True"},
#                                  {"indexID": 6, "firstName": "Rachna", "canVote": "True", "canDrive": "True"}
#                             ]
#     }
# ]

# cityName = str(input("Enter city ")).lower()

# def getCityNames(c):
#     if str(c["city"]).lower() == cityName:
#         return True
#     else:
#         return False

# c = list(filter(getCityNames,employees))

# for x in c:
#     for cnt in range(0, len(x["emp"])):
#         print(x["emp"][cnt]["firstName"])
