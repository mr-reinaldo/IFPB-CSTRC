"""
    Escreva um programa para ler vários números. O programa deverá
    encerrar quando forem informados 06 (seis) números distintos, ou seja,
    não repetem. Ao final, evaloriba todos os números lidos.
"""
numeros = []
count_dins = 0

while(count_dins != 6):
    valor = int(input("Digite numero: "))
    if (valor not in numeros):
        numeros.append(valor)
        count_dins += 1
        print(count_dins)

print("\nNumeros lidos: ")
for value in numeros:
    print(value, end=" ")
print()
