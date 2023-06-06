"""
Fibonacci linear
por Danrley Ribeiro
"""


def check_n(n):
    while n < 0:
        return check_n(int(input("Valor inválido. Digite novamente: ")))
    return n


def fib(n):
    ult = 1
    penult = 1
    at = 0
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(2, n):
            at = ult + penult
            penult = ult
            ult = at
        return at


num = check_n(int(input("Digite o termo a encontrar: ")))
resultado = fib(num)
print(f"fib({num}) = {resultado}")
