"""
Numeros primos utilizando recursividade
por Danrley Ribeiro
"""


def check_n(n):
    while n <= 0:
        return check_n(int(input("Valor inválido. Digite novamente: ")))
    return n


def primo(n):
    pass
