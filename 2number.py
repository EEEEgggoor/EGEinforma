def f(x, y, z, w):
    return (not(x<=w) or (y==z) or y) #<<<логическое выражение из задания

print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if f(x, y, z, w) == 0:
                    print(x, y, z, w)