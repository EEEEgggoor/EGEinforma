# f3 = open('24_1.txt').readline()
# k = 1
# m = 0
# for i in range(len(f3)):
#     if f3[i] == 'Z' and f3[i - 1] == 'Z':
#         k += 1
#         m = max(k, m)
#     else:
#         k = 1
# m = max(k, m)
# print(m)


# f3 = open('24_2.txt').readline()
# k = 1
# m = 0
# for i in range(len(f3)):
#     if f3[i] == 'A' and f3[i - 1] == 'B':
#         k += 1
#         m = max(k, m)
#     else:
#         k = 1
# m = max(k, m)
# print(m)


# from collections import Counter
#
#
# f3 = open('24_3.txt').readline()
# sp1=[]
# for i in range(len(f3)-1):
#     if f3[i]=='A' and f3[i+1]!='A':
#         sp1.append(f3[i+1])
# sp1 = sorted(sp1)
# print(Counter(sp1).most_common(1))


# from collections import Counter
#
#
# f3 = open('24_4.txt').readline()
# sp1=[]
# for i in range(len(f3)-2):
#     if f3[i]==f3[i+1]!=f3[i+2]:
#         sp1.append(f3[i+2])
# sp1 = sorted(sp1)
# print(Counter(sp1).most_common(1))


# f3 = open('24_5.txt').readline()
# k = 1
# m = 0
# for i in range(len(f3)):
#     if f3[i-1]==f3[i]:
#         k+=1
#         m = max(m, k)
#     else:
#         k=1
# m = max(k, m)
# print(m)

#
# f3 = open('24_6.txt').readline()
# k=1
# m=0
# for i in range(len(f3)-1):
#     if (f3[i+1]!='K' and f3[i]!='L') or (f3[i+1]!='L' and f3[i]!='K'):
#         k+=1
#         m = max(m, k)
#     else:
#         k=1
# m = max(m, k)
# print(m)



