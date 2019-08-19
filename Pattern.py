n = 123
num = []
first = True
while (n > 0):
    if first:
        num.append(n % 2)
        n = (n // 2)
        first=False
    else:
        num.append(n % 2)
        n = (n // 2)
num.reverse()
print(num)



y=1234
while (y >0):
    a = (y % 10)
    y = (y // 10)
    print(a)
    



for x in range(1,9):
    for y in range(x,9):
        print(y, end="")
    print()



n = int(input("Enter number "))
num = []
first = True
while (n > 0):
    if first:
        num.append(n % 2)
        n = (n // 2)
        first=False
    else:
        num.append(n % 2)
        n = (n // 2)
num.reverse()
print(num)
   