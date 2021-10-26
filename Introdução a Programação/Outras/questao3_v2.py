"""
    Escreva um programa para ler uma string. Analise o texto lido
    e exiba se esse texto é formado apenas por dígitos numéricos.
"""

texto = input()

if texto.isdigit():
    print('Sim')
else:
    print('Não')
