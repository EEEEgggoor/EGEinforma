from ipaddress import *

'''23) - ДЕМО2023.2024'''
# k = 0
# nt = ip_network('192.168.32.160/255.255.255.240')
# for ip in nt:
#     if bin(int(ip)).count('1')%2:
#         k+=1
#
#
# print(k)


# k=0
# for i in range(32):
#     net = ip_network('71.192.0.12/' + str(i), 0)
#     sb = str(net).split('/')
#     if sb[0]=='71.192.0.0':
#         k+=1
# print(k)
# Ответ:19

# k=0
# #reshu ege - 15134
# for i in range(32):
#     nt = ip_network('93.138.161.49/' + str(i), 0)
#     s = str(nt).split('/')
#     if s[0]=='93.138.160.0':
#         k+=1
# print(k)
