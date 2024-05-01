f = open('f5')
n = int(f.readline())
f = [tuple(map(int, x.split())) for x in f]
a=[]
sp = []
for i in range(n):
    num = f[i][0]
    kount = f[i][1]
    k = kount//100 if kount%100==0 else kount//100+1
    a.append((num, k))
for i in range(n):
    centr = a[i][0]
    sm = 0
    for j in range(n):
        sm += abs(centr-a[j][0])*a[j][1]
    sp.append(sm)
print(min(sp))