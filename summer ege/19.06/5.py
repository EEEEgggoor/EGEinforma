d=0
for N in range(1001, 9999, 2):
    p=[]
    n = str(N)
    n0 = int(n[0])
    n1 = int(n[1])
    n2 = int(n[2])
    n3 = int(n[3])
    s1, s2, = n0+n1, n2 + n3
    p.append(s1)
    p.append(s2)
    k = str(min(p))+str(max(p))
    if k=='616':
        d+=1
print(d)

