# решу егэ - 10290

# s= '1' + '8' * 80
# while '18' in s or '288' in s or '3888' in s:
#     s = s.replace('18', '2', 1)
#     s = s.replace('288', '3', 1)
#     s = s.replace('3888', '1', 1)
# print(s)


# дз на 24.04.23

s = '1' * 95 + '7' * 31
while '1111' in s:
    s = s.replace('1111', '7', 1)
    s = s.replace('77', '1', 1)
print(s)
