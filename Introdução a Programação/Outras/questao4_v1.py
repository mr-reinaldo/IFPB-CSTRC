"""
    Escreva um programa para ler um número inteiro. O programa
    só deverá encerrar quando o usuário digitar um valor numérico
    inteiro. Ao final, exiba o número lido.
"""
verificador = 0
while verificador == 0:
    numero = input()
    for c in numero:
        if ord(c) < ord('0') or ord(c) > ord('9'):
            break
    else:
        verificador += 1
print(numero)
