"""
    Escreva um programa para ler 10 (dez) números. Ao final, exiba todos
    os valores lidos que são maiores do que o último número lido.

"""
numeros = []
for i in range(10):
    valor = int(input("["+str(i)+"] Digite numero: "))
    numeros.append(valor)

for value in numeros:
    if(value > numeros[-1]):
        print(value)
