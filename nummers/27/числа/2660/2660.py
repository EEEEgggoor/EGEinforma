f = open('27-a.txt')
n = int(f.readline())
f = ([list(map(int, x.split())) for x in f])
mx = []
for i in range(n):
    mx.append(max(f[i]))
sm = sum(mx)
otv = []
for i in range(n):
    sm1 = sm - max(f[i]) + min(f[i])
    if sm1%3!=0:
        otv.append(sm1)
print(max(otv))
