f = open('27-161a.txt')
N, V = map(int, f.readline().split())
a = []
for i in range(N):
    k = int(f.readline())
    c = k//V if k%V==0 else k//V + 1
    a.append(c)

print(a)