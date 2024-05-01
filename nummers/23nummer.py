# Поляков №26

# def f3(start, finish):
#     if start>finish or start==25: return 0
#     if start==finish: return 1
#     if start<finish: return f3(start+1, finish) + f3(start*2, finish)
#
#
# print(f3(2, 14) * f3(14, 29))


# Поляков №445
# def F(s, f3):
#     if s>f3 or s==10: return 0
#     if s==f3: return 1
#     if s<f3: return F(s+1, f3) + F(s*2, f3)
#
# print(F(1, 21))


# Поляков №446
# def F(s, f3):
#     if s>f3: return 0
#     if s==f3: return 1
#     if s<f3: return F(s+1, f3) + F(s*2, f3)
#
#
# print(F(4, 11)+F(4, 22))
