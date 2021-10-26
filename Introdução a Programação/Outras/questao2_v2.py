"""
    Escreva um programa para ler uma frase. Analise o texto lido e exiba
    a quantidade de vogais encontradas.
"""
frase = input()

count = 0
vogais = "aeiou"

for s in frase:
    if s in vogais or s in vogais.upper():
        count += 1


print(count)
