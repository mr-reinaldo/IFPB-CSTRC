"""
    Escreva um programa para ler uma string. Analise o texto lido
    e exiba se esse texto é formado apenas por dígitos numéricos.
"""

texto = input()
# verify = 0

for c in texto:
    if ord(c) < ord('0') or ord(c) > ord('9'):
        print('Não')
        break
else:
    print('Sim')
