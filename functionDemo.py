def fn():
    a = 'Do you really want to quit?'
    
    ok = input(a)
    if ok in ('y', 'ye', 'yes'):
         print("Yes")
    else:
         print("No")
   

fn()
# fn('Do you really want to quit?')
