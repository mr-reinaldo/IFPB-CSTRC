"""
    Escreva um programa para ler um número inteiro. O programa
    só deverá encerrar quando o usuário digitar um valor numérico
    inteiro. Ao final, exiba o número lido.
"""


while True:
    numero = input()

    if numero.isdigit():
        break

print(numero)
