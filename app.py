char = ['a', 'f', 's', 'd', 'a', 's', 'f', 's', 'f', 'g']

def getChar(c):
    if c == 's':
        return True
    else:
        return False

c = list(filter(getChar, char))

print(c)

