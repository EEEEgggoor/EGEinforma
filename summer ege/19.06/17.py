l = [int(i) for i in open('17.txt')]
p = []
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] % 160 != l[j] % 160) and ((l[i] % 7 == 0) or (l[j] % 7 == 0)):
            p.append(l[i] + l[j])
print(len(p), max(p))