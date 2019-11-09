# www = "www.google.com"

# d = dict()

# d['google'] = ["www.google.com","www.gmail.com","www.youtube.com"]
# d["oracle"] = ["www.oracle.com", "www.mySQL.com","www.oracleNoSQL.com"]


# for key, value in d.items():
#     print(f'{key} {value}')
#     print()


numbers = (2,3,4,6,5,2,4,7,34,5,76,56,23,13,67,54,23,46,13,57,53,43,24,35,7)

# def fn(n):
#     return (n)

x = map(lambda n :n if n > 50 else '', numbers)

for key, value in enumerate(x):
    print(f'{key} {value}')
