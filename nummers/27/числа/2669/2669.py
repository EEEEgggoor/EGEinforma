f = open('27-b.txt')
n = int(f.readline())
f = [int(x) for x in f]
otv = []
for i in range(n-6):
    for j in range(i+6, n):
        if (f[j]*f[j])%2==0:
            otv.append(f[i]*f[j])
print(min(otv))