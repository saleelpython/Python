#!C:\Users\saleel\AppData\Local\Programs\Python\Python37-32\python

person = {"ID": "1001", "firstName": "Saleel", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}

l = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def fn(l):
    x = iter(l)

    while True:
        try:
            print(next(x))
        except StopIteration as ex:
            print('-' * 16)
            print("data not Dound")
            break

fn(l)








        