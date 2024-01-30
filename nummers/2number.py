# def f(x, y, z):
#     return ((x == z) or (( x<= (y and z))))  #<<<логическое выражение из задания
#
# print('x y z')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             if f(x, y, z) == 0:
#                 print(x, y, z)


# def f(x, y, z, w):
#     return ((z and y) or ((x <= z) == (y <= w)))  #<<<логическое выражение из задания
#
# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if f(x, y, z, w) == 0:
#                     print(x, y, z, w)


def f(x, y, z, w):
    return w or (x <= y) and (not z <= x)


print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if f(x, y, z, w) == 0:
                    print(x, y, z, w)
