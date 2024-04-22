f = open('27-1a.txt')
n, m = map(int, f.readline().split())
a = []
for i in range(n):
    km, otp = (map(int, f.readline().split()))
    r = otp//50 if otp%50==0 else otp//50+1
    a.append((km, r))
mx = -100
for i in range(n):
    sklad = a[i][0]
    sm = 0
    for j in range(n):
        if abs(sklad - a[j][0])<=m:
            sm += a[j][1]
    mx = max(mx, sm)
print(mx)