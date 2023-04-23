"""for x in range(10001, 100000):
    x = str(x)
    s = int(x[0]) + int(x[2]) + int(x[4])
    s1 = int(x[1]) + int(x[3])
    n = str(s1) + str(s)
    if n == '621':
        print(x)
        break"""

'''for N in range(100):
    k = 0
    n2 = bin(N)[2:]
    n2 += str(n2.count('1')%2)
    n2 += str(n2.count('1') % 2)
    R = int(n2, 2)
    if R > 125:
        print(N)'''


# for N in range(100):
#     n2 = bin(N)[2:]
#     if n2.count('1')%2==0:
#         k = '10' + n2[2:] + '0'
#     else:
#         k = '11' + n2[2:] + '1'
#     if int(k, 2)>40:
#         print(N)


for N in range(1, 100):
    n2 = bin(N)[2:]
    N2 = n2 + n2[-1]
    if n2.count('1')%2==0:
        N2 = N2 + '0'
    else:
        N2 = N2 + '1'

    if N2.count('1')%2==0:
        N2 = N2 + '0'
    else:
        N2 = N2 + '1'
    if int(N2, 2)>130:
        print(N)
        break