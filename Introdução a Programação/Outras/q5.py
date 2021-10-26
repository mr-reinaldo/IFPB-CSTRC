"""
    Escreva um programa para ler vários números. O programa deverá
    encerrar quando forem informados 06 (seis) números pares. Ao final,
    exiba todos os números pares lidos.
"""
numeros = []
count_par = 0

while(count_par != 6):
    valor = int(input("Digite numero: "))
    numeros.append(valor)

    if (valor % 2 == 0):
        count_par += 1
    print(f'{count_par} par')

print("\nNumeros pares lidos: ")
for value in numeros:
    if (value % 2 == 0):
        print(value, end=" ")
print()
