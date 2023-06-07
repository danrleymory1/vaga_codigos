"""
Numeros primos linear
por Danrley Ribeiro
"""


def check_num(n):
    while n < 1:
        return check_num(int(input("Valor inválido. Digite novamente: ")))
    return n


def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


lista = []
num = check_num(int(input()))
for j in range(num+1):
    if primo(j):
        lista.append(j)

print(f"p({num}) = {lista}")
