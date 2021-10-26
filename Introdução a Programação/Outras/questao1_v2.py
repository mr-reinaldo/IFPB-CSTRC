"""
    Escreva um programa para ler uma frase. Analise o texto lido e
    exiba a quantidade de caracteresespeciais encontrados.
"""
frase = input()

count = 0


for s in frase:
    if not s.isalpha() and not s.isalnum():
        count += 1

print(count)
