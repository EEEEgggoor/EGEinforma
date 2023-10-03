import site


def f(a):
    s = set()
    for i in range(1, int(a**0.5)+1):
        if a%i==0:
            s.add(i)
            s.add(a//i)
    return sorted(s)


#2568 - polyakov
# for i in range(164700, 164752+1):
#     if len(f(i))==6:
#         print(f(i)[4:])



#2562 - polyakov
# for i in range(174457, 174505+1):
#     if len(f(i))==4:
#         print(f(i)[1:-1])

p=[]
s=[]
for i in range(113_000_000, 114_000_000+1):
    k=0
    for j in range(len(f(i))):
        if f(i)[j]%2==0:
            k+=1
        if k==3:
            s.append(i)
            p.append(f(i)[1])
            break

print(s, p)
