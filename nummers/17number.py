# ans = []
# l = [int(i) for i in open('17.txt')]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i] + l[j]%8==0):
#             ans.append(l[i] + l[j])
# print(len(ans), max(ans))

ans = []
mn=[]
k=0
l = [int(i) for i in open('17_1.txt')]
for i in range(len(l)-2):
    if (l[i] % 12 == 0 or l[i+1] % 12 == 0 or l[i+2] % 12 == 0) and (l[i] % 3 == 0 and l[i+1] % 3 == 0 and l[i+2] % 3 == 0):
        mn.append(((l[i]) + (l[i+1]) + (l[i+2]))/3)
        k+=1
print(k, min(mn))
