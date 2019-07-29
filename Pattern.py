while (y >0):
    a = (y % 10)
    y = round(y // 10)
    print(a)
    

for x in range(1,9):
    for y in range(x,9):
        print(y, end="")
    print()