f = open("27-B.txt")
n = int(f.readline())
k = [[0]*11 for i in range(3)]
for i in range(n):
    x = int(f.readline())
    k[x%3]+=1
