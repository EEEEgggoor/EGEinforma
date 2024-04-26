f = open('27-a.txt')
n, k, m = map(int, f.readline().split())
a = []
for i in range(n):
    km, mail = map(int, f.readline().split())
    K = mail//20 if mail%20==0 else mail//20+1
    a.append((km, K))
a.sort()
d = [0]* (k+1)
for i in range(n):
    d[a[i][0]] = a[i][1]

d[0] = d[-1]
sp = []
for i in range(m, k-(m+1)):
    s=0
    if d[i]==0:
        if sum(d[i-m:i+(m+1)])==0:
            for j in range(k):
                s+=min(abs(i-j)*d[j], (k-abs(i-j))*d[j])
            sp.append((s, i))
print((sp))
print(min(sp))

