"""
Fibonacci utilizando recursividade
por Danrley Ribeiro
"""


def check_n(n):
    while n < 0:
        return check_n(int(input("Valor inválido. Digite novamente: ")))
    return n


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


num = check_n(int(input("Digite o termo a encontrar: ")))
resultado = fib(num)
print(f"fib({num}) = {resultado}")
