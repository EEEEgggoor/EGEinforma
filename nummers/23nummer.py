# Поляков №26

# def f(start, finish):
#     if start>finish or start==25: return 0
#     if start==finish: return 1
#     if start<finish: return f(start+1, finish) + f(start*2, finish)
#
#
# print(f(2, 14) * f(14, 29))


# Поляков №445
# def F(s, f):
#     if s>f or s==10: return 0
#     if s==f: return 1
#     if s<f: return F(s+1, f) + F(s*2, f)
#
# print(F(1, 21))


# Поляков №446
# def F(s, f):
#     if s>f: return 0
#     if s==f: return 1
#     if s<f: return F(s+1, f) + F(s*2, f)
#
#
# print(F(4, 11)+F(4, 22))
