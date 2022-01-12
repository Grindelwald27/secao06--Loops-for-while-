for n in range(1000, 10000):
    w = str(n)
    x = w[0:2]
    y = w[2:]
    z = int(x) + int(y)
    if z ** 2 == n:
        print(n)
