def f(x, y, a):
    return (3*x + 4*y != 70) or (a>x) or (a>y)
for a in range(0, 1000):
    fl = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if f(x, y, a)==False:
                fl = False
                break
        if fl == False:
            fl = False
            break
    if fl == True:
        print(a)
        break