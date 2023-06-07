"""
Numeros primos utilizando recursividade
por Danrley Ribeiro
"""


def check_num(n):
    while n < 1:
        return check_num(int(input("Valor inválido. Digite novamente: ")))
    return n


def primo(n, divisor=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True

    return primo(n, divisor + 1)


lista = []
num = int(input())
for i in range(num+1):
    if primo(i):
        lista.append(i)

print(f"p({num}) = {lista}")
