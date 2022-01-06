def somar(*soma):
    s = 0
    for num in soma:
        s += num
    print(s)


somar(2, 2)
somar(3, 3, 3)