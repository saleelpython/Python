www = "www.google.com"

d = dict()

for i in range(len(www)):
    d.setdefault(www[i], www.count(www[i]))

print(d)

