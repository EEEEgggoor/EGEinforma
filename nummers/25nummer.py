from fnmatch import *
for i in range(0, 10**10, 73):
    if fnmatch(str(i), '12345*76'):
        print(i, i//73)