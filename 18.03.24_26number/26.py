# f = open('26-7356.txt')
# n = f.readline()
# f = [list(map(int, x.split())) for x in f]
# f.sort(reverse=True)
# f = f[1:]
# kup = 8*24
# minikup = 8*24
# det = 0
#
#
# for i in f:
#     if i[0]>2 and (kup>0):
#         kup+=1
#         det+=i[1]
#     if i[0]<=2 and (kup>0):
#         kup-=1
#         det+=i[1]
# print(det)


f = [int(x) for x in open('26-45.txt')]
f = f[1:]
sp = []
for i in range(len(f)):
    for j in range(len(f)):
        if (f[i]+f[j])%2==0 and ((f[i]+f[j])//2 in f):
            sp.append(f[i]+f[j])
print(len(sp))