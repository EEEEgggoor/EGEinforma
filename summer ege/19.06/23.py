def F(s, f):
    if s<f: return 0
    if s==f: return 1
    if s>f: return F(s-1, f) + F(s//2, f)

print(F(78, 16) * F(16, 4))