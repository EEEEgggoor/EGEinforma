# КЕГЭ - 6056
# s = [int(x) for x in open('26.txt')][1:]
# s = sorted(s, reverse=True)
# k, mini = 1, s[0]
# for i in range(1, len(s)):
#     if s[i] + 56 <= mini:
#         mini = s[i]
#         k += 1
# print(k, mini)


# КЕГЭ - 5228
# s = [int(x) for x in open('26_1.txt')][1:]
# s = sorted(s, reverse=True)
# k, mx = 1, s[0]  # начинаем с первого передачика, потому k=1
# for i in range(0, len(s)):
#     if s[i] + 8 <= mx:
#         mx = s[i]
#         k += 1
# print(k, mx)


#  поляков - 5325
# s = [int(x) for x in open('26-2.txt')][1:]
# s = sorted(s, reverse=True)
# k, mx = 1, s[0]
# for i in range(0, len(s)):
#     if s[i]+3<=mx:
#         mx = s[i]
#         k+=1
# print(k ,mx)


# КЭГЭ - 2686
f = open('26_3.txt')
k = f.readline()
s = [list(map(int, x.split())) for x in f]
s = sorted(s)
k=0
for i in range(len(s)):
    if s[i][0]==s[i-1][0] and s[i][1]-s[i-1][1]==1:
        k+=1
        if k>=5:
            print(s[i])
    else:
        k=0
