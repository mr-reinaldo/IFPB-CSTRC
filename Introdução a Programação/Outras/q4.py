"""
    Escreva um programa para ler (06) números. Ao final, exiba todos
    os valores lidos que são maiores doque a média dos números lidos.
"""
numeros = []
media = 0.0

for i in range(6):
    valor = int(input("["+str(i)+"] Digite numero: "))
    numeros.append(valor)

for values in numeros:
    media += values

media /= len(numeros)

print(f"\nMédia: {media}\nNumeros maiores que a média:")

for values in numeros:
    if(values > media):
        print(values, end=" ")
print()
