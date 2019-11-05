fruits = [('orange','banana','kiwi'),('banana','apple'),('blackberry','blueberry'), ('lime', 'kiwi', 'apple')]




f = list()
cnt=0
def fn(l):
   for i in range(len(l)):
      if l[i][0] not in f:
         f.append((l[i]))
      
fn(fruits)
print(f)

