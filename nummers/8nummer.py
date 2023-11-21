from itertools import *

# Поляков - 6272
# a - 10
# b - 13
# c - 16
# d - 19
# k=0
# a=[]
# for j in range(2, 5):
#     for i in combinations('ABCD', r=j):
#         s = ''.join(i)
#         a.append(s)
#
# for i in product(a, repeat=3):
#     s1=''.join(i)
#     if s1.count('B')>1:
#         k+=1
# print(k)


# Поляков 6342
# s = 'добрыня'
# k = 0
# for i in permutations(s, 6):
#     s = ''.join(i)
#     s = s.replace('о', "*").replace('ы', "*").replace('я', "*")
#     if s.count('*') < (6 - s.count('*')) and '**' not in s:
#         k+=1
# print(k)


