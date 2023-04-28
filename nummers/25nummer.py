#компегэ   №7601
# from fnmatch import *
# for x in range(0, 10**8+1, 273):
#     if fnmatch(str(x), '12??36*1'):
#         print(x, x // 273)

# for c1 in '0123456789':  #<<< второй способ работы
#                               задачи выше
#     for c2 in ('0123456789'):
#         a = int(f'12{c1}{c2}361')
#         if a%273==0:
#             print(a, a//273)
# for c1 in '0123456789':
#     for c2 in ('0123456789'):
#         for c3 in ('0123456789'):
#             a = int(f'12{c1}{c2}36{c3}1')
#             if a%273==0:
#                 print(a, a//273)


#поляков №2562
def div(n):
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)
#
#
# for i in range(174457, 174505+1):
#     if len(div(i)) == 2:
#         print(div(i), div(i)[0]*div(i)[1])


# поляков №2572
# for i in range(190201, 190260+1):
#     sp = []
#     for j in div(i):
#         if j%2==0:
#             sp.append(j)
#     if len(sp) == 4:
#         print(sp[-1], sp[-2])


#поляков №2575
# for i in range(244143, 1367821+1):
#     sp = []
#     if len(div(i)) == 5:
#         print(div(i)[-3], div(i)[-2])
