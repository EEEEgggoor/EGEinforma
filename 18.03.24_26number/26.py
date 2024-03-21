f = [int(x) for x in open('26_3761.txt')]
f = f[1:]




mx=-11111
k=0
for i in range(len(f)-1):
    for j in range(i+1, len(f)):
        sm = f[i]+f[j]
        if (sm%2==0) and sm//2 in f:
            k+=1
            mx = max(mx, sm//2)
print(k, mx)


