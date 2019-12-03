import module2
import csv
import json
import pandas
import os


# person = [
#     {"_id":1, "indexID": "1001", "firstName": "Saleel", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
#     {"_id":2,"indexID": "1002", "firstName": "Vrushali", "lastName": "Bagde", "canVote": "True", "canDrive": "False"}, 
#     {"_id":3,"indexID": "1003", "firstName": "Sharmin", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
#     {"_id":4,"indexID": "1004", "firstName": "Nitish", "lastName": "Patil", "canVote": "True", "canDrive": "True"}, 
#     {"_id":5,"indexID": "1005", "firstName": "Neel", "lastName": "Save", "canVote": "False", "canDrive": "True"}, 
#     {"_id":6,"indexID": "1006", "firstName": "Deep", "lastName": "Save", "canVote": "False", "canDrive": "False"}, 
#     {"_id":7,"indexID": "1007", "firstName": "Ruhan", "lastName": "Bagde", "canVote": "False", "canDrive": "False"}
# ]

#region Main 
# countries = ["India", "Indonesia", "Thailand", "Sri Lanka", "Comoros", "Saudi Arabia", "South Africa", "Djibouti", "France", "Malaysia", "Vietnam", "Maldives", "Oman", "Kuwait", "Eritrea", "Mozambique", "Australia", "Myanmar", "Brunei", "Mauritius", "Iran", "Bahrain", "Sudan", "Somalia", "New Zealand", "Philippines", "Cambodia", "Madagascar", "UAE", "Israel", "Kenya", "USA", "Japan", "Singapore", "Bangladesh", "Seychelles", "Qatar", "Egypt", "Tanzania", "UK", "South Korea", "Russia", "Israel", "Tajikistan", "Jordan", "Lebanon", "Panama", "Jamaica", "Namibia", "Botswana", "Fiji", "Uruguay", "Kuwait", "Denmark", "Palestine", "Mongolia", "Kosovo", "Cyprus", "Bahamas", "Marshall Islands", "Greenland", "Iceland", "Greece", "Portugal", "Belgium", "Zambia", "Zimbabwe", "Netherlands", "Syria", "Argentina", "Tanzania", "Spain", "Ukraine", "Kenya", "Uganda", "Uzbekistan", "Afghanistan", "Madagascar", "Romania", "Kazakhstan"]

# def getData(l):
#     for i in l:
#         yield i

# x = getData(countries)

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

#endregion
#-------------------------------------------------------------------------

#region CSV

#Region,	Country, ItemType, SalesChannel, OrderPriority, OrderDate, OrderID, ShipDate, UnitsSold, UnitPrice, UnitCost, TotalRevenue', TotalCost, TotalProfit
# l = list()
# with open ("Sales.csv" ,'r') as fs:
#     data = csv.reader(fs)
  
#     for i in data:
#         l.append({"Region":i[0], "Country":i[1], "ItemType":i[2], "SalesChannel":i[3], "OrderPriority":i[4], "OrderDate":i[5], "OrderID":int(i[6]), "ShipDate":i[7], "UnitsSold": int(i[8]), "UnitPrice":float( i[9]), "UnitCost": float(i[10]), "TotalRevenue":float(i[11]), "TotalCost":float(i[12]), "TotalProfit": float(i[13])})

# for i in range(len(l)):
#     print(l[i])
#     print('-' * 55)
#endregion

#-------------------------------------------------------------------------

#region Functions

# def fn(a, b):
#     return ({"_ID":a, "fullName":b})

# x = fn(1001, 'saleel bagde')
# print(x)

# y = fn(a=1002, b='sharmin bagde')

# print(y)



#endregion

#-------------------------------------------------------------------------

#region List Comprehensions 



#endregion

#-------------------------------------------------------------------------

#region Pandas 
pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)
pandas.set_option("display.width", None)



# with open("weather.csv" , 'r') as fs:
df = pandas.read_csv("movie.csv", names=["color", "director","critic","duration","director_facebook","actor_3_facebook","actor_2_name",	"actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords",	"movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes"], header=None )

# df.fillna('Not Available', inplace=True)
df.fillna(value={"color": "Color", "critic": 450, "director":"Not Available", "director_facebook":"Not Available"}, inplace=True)
# print(df.columns)

print()
print()
# print(df["duration"].max())
# print(df["duration"].min())
# print(df[["color", "director","movie_title","critic","duration","director_facebook","actor_3_facebook","actor_2_name"]][df["duration"] == 150])
# print(df[["color", "director","movie_title","critic","duration","director_facebook","actor_3_facebook","actor_2_name"]][df["duration"] >= 450])
# print(df[["color", "director","movie_title","critic","duration","director_facebook","actor_3_facebook","actor_2_name"]][df["duration"] == df["duration"].max()])
# print(df[["color", "director","movie_title","critic","duration","director_facebook","actor_3_facebook","actor_2_name"]][df["duration"] == df["duration"].min()])



# print()
# print()

# print(df.director)

#endregion





