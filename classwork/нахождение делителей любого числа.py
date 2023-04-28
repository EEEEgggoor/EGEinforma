def div(n):
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)

    return sorted(d)


print(div(128))

