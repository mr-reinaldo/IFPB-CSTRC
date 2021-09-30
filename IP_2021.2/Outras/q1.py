"""
    Escreva um programa para ler 06 (seis) números.
    Ao final, exiba todos os números lidos.

"""

numeros = []
for i in range(6):
    numeros.append(input("["+str(i)+"] Digite numero: "))
for values in numeros:
    print(values)
