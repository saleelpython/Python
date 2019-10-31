l = [i for i in range(1,11) if i < 7]

for key, value in enumerate(l, start=100):
    print(f'{key} {value}')