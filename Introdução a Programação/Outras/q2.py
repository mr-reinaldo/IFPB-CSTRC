"""
    Escreva um programa para ler (06) números. Ao final, exiba todos os
    números lidos na ordem inversa.

"""
numeros = []
for i in range(6):
    numeros.append(input("["+str(i)+"] Digite numero: "))

for i in numeros[::-1]:
    print(i)
