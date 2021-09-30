"""
    Escreva um programa para ler uma frase. Analise o texto lido e
    exiba a quantidade de caracteresespeciais encontrados.
"""
frase = input()

count = 0
# a-z -> 97 - 122
# A-Z -> 65 - 90
# 0-9 -> 48 - 57

for s in frase:
    if s < '0' or s > '9' \
        and s < 'A' or s > 'Z' \
            and s < 'a' or s > 'z':
        count += 1

print(count)
