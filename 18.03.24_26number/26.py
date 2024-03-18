f = open('26-7356.txt')
n = f.readline()
f = [list(map(int, x.split())) for x in f]
f.sort(reverse=True)
f = f[1:]
kup = 8*24
minikup = 8*24
det = 0


for i in f:
    if i[0]>2 and (kup>0):
        kup+=1
        det+=i[1]
    if i[0]<=2 and (kup>0):
        kup-=1
        det+=i[1]
print(det)