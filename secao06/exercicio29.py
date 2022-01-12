from math import factorial
n = 10
s = 0
denominador = 0
for i in range(2, n + 1, 2):
    denominador = denominador + 1
    razao = denominador / factorial(i)
    s = s + razao
print(s)
