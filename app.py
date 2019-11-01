time = int(input("Enter Time "))

def fn1(t):
    if t >= 1 and t <= 6 :
       print("day")
    else:
       print('sorry there no available driver around you!')

def fn2(t):
    if t >= 7 and t <= 12 :
       print("night")
    else:
       print('sorry there no available driver around you!!')

def main(a):
    fn1(a)
    fn2(a)

main(time)

