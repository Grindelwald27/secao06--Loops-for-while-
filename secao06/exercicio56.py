soma = 0
for n in range(2, 2000000):
    for i in range(2, n):
        if n % i == 0:
            break
        else:
            soma += n
print(soma)
