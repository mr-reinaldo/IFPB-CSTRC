"""
    Escreva um programa para ler uma frase. Analise o texto lido e exiba
    a quantidade de vogais encontradas.
"""
frase = input()

count = 0

for s in frase:
    if s in "aeiouAEIOU":
        count += 1


print(count)
