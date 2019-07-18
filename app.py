#!C:\Users\saleel\AppData\Local\Programs\Python\Python37-32\python
# Comprehensions in Python
# fruit = ['blackberry', 'grapes', 'blueberry', 'fig', 'lemon', 'watermelon', 'apple', 'kiwi', 'lime', 'mango','blackberry']

names = ['saleel', 'vrushali', 'sharmin']
number = [ 1, 4, 3]

fn = lambda name: (x for x in zip(number, names))

for x in fn(names):
    print(x)
