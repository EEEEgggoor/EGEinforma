s = 40 * "7" + 40 * '9' + 50 * '4'
while ('49' in s) or ('97' in s) or ('47' in s):
    s = s.replace('47', '74', 1)
    s = s.replace('97', '79', 1)
    s = s.replace('49', '94', 1)
print(s[25] + s[71] + s[105])