for x in range(10001, 100000):
    x = str(x)
    s = int(x[0]) + int(x[2]) + int(x[4])
    s1 = int(x[1]) + int(x[3])
    n = str(s1) + str(s)
    if n == '621':
        print(x)
        break
