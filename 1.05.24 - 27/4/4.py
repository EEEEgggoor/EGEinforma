f = open('27A_4.txt')
n, m = map(int, f.readline().split())
f = [int(x) for x in f]
sp = []
for i in range(n):
    s = 0
    for j in range(n):
        if abs(j-i)<=m: s+=f[i]
    sp.append(s)
print(max(sp))