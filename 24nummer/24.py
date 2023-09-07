# f = open('24_1.txt').readline()
# k = 1
# m = 0
# for i in range(len(f)):
#     if f[i] == 'Z' and f[i - 1] == 'Z':
#         k += 1
#         m = max(k, m)
#     else:
#         k = 1
# m = max(k, m)
# print(m)


# f = open('24_2.txt').readline()
# k = 1
# m = 0
# for i in range(len(f)):
#     if f[i] == 'A' and f[i - 1] == 'B':
#         k += 1
#         m = max(k, m)
#     else:
#         k = 1
# m = max(k, m)
# print(m)


# from collections import Counter
#
#
# f = open('24_3.txt').readline()
# sp1=[]
# for i in range(len(f)-1):
#     if f[i]=='A' and f[i+1]!='A':
#         sp1.append(f[i+1])
# sp1 = sorted(sp1)
# print(Counter(sp1).most_common(1))


# from collections import Counter
#
#
# f = open('24_4.txt').readline()
# sp1=[]
# for i in range(len(f)-2):
#     if f[i]==f[i+1]!=f[i+2]:
#         sp1.append(f[i+2])
# sp1 = sorted(sp1)
# print(Counter(sp1).most_common(1))


# f = open('24_5.txt').readline()
# k = 1
# m = 0
# for i in range(len(f)):
#     if f[i-1]==f[i]:
#         k+=1
#         m = max(m, k)
#     else:
#         k=1
# m = max(k, m)
# print(m)

#
# f = open('24_6.txt').readline()
# k=1
# m=0
# for i in range(len(f)-1):
#     if (f[i+1]!='K' and f[i]!='L') or (f[i+1]!='L' and f[i]!='K'):
#         k+=1
#         m = max(m, k)
#     else:
#         k=1
# m = max(m, k)
# print(m)



