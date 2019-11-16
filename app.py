# import json

# with open ("Person.json", "r") as fs:
#     data = json.load(fs)
#     print(data)


# def fn(a, b):
#     return a >= b

# print(fn('a', 'a'))

# numbers = [1, 2, 3, 4, 5, 6, 7]
# x = 0
# for i in numbers:
#     x = x + i
#     print(f'{x=}  {i=}')

fruits = ['blackberry', 'grapes', 'blueberry', 'fig', 'lemon', 'watermelon', 'apple', 'kiwi', 'lime', 'mango','blackberry']

x = fruits.__iter__()

while True:
    try:
        print(x.__next__())
    except StopIteration:
        print('done')
        break