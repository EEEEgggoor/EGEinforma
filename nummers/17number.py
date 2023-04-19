ans = []
l = [int(i) for i in open('17.txt')]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] + l[j]%8==0):
            ans.append(l[i] + l[j])
print(len(ans), max(ans))
