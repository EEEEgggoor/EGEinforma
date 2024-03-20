# f = [int(x) for x in open('26-45.txt')]
# f = f[1:]
# sp = []
# f.sort()
#
#
# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys)-1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first+last)//2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val<lys[mid]:
#                 last = mid -1
#             else:
#                 first = mid +1
#     if index!=-1:
#         return True
#     if index==-1:
#         return False
# mx=-11111
# k=0
# for i in range(len(f)):
#     for j in range(i, len(f)-1):
#         if (f[i]+f[j])%2==0 and BinarySearch(f, (f[i]+f[j])/2):
#             k+=1
#             mx = max(mx, (f[i]+f[j])/2)
# print(k, mx)

