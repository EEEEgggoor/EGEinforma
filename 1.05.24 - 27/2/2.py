f = open('27A_2.txt')
k = int(f.readline())
n = int(f.readline())
f = [int(x) for x in f]
sp = []
for i in range(n):
    for j in range(i, n):
        if j-i>=k and (f[i]+f[j])%2!=0:
            sp.append(f[i]+f[j])
print(max(sp))