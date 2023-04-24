ans = []
k=0
l = [int(i) for i in open('17_2.txt')]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if ((l[i] + l[j])%120==0):
            k+=1
            ans.append(l[i] + l[j])
print(len(ans), max(ans))

# ans = []
# k=0
# l = [int(i) for i in open('17_3.txt')]
# for i in range(len(l) - 1):
#     if ((l[i]+l[i+1])%7==0) and (l[i]%5==0 or l[i+1]%5==0):
#         ans.append(l[i]+l[i+1])
#         k+=1
# print(k, max(ans))

# ans = []
# k=0
# l = [int(i) for i in open('17_4.txt')]
# for i in range(len(l) - 2):
#     if (l[i]**2==l[i+1]**2 + l[i+2]**2) or (l[i+1]**2==l[i]**2 + l[i+2]**2) or (l[i+2]**2==l[i+1]**2 + l[i]**2):
#         ans.append(l[i]+l[i+1]+l[i+2])
#         k+=1
# print(k, ans)

