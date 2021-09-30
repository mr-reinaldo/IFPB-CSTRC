#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor: José Reinaldo
# Descrição: Atividade para a disciplina de Introduçãoa Programação.

from random import randint
import ifbet as fb

sorteados = []
cartelas = []
contador = 0

fb.limpar()
fb.banner()
saida = int(input("Quantidade de Jogadores: "))
for i in range(saida):
    cartelas.append(fb.novo(1, 10))

while contador <= 0:
    fb.limpar()
    fb.banner()
    numero = randint(1, 10)
    if (fb.contido(numero, sorteados)):
        continue
    else:
        fb.inserir(numero, sorteados)
        print("Numero Sorteado: {}".format(numero))
        for cartela in cartelas:
            print(f"\033[36m{cartela}\033[0;0m  Marcou: {fb.verificar(cartela, sorteados)} Números")
            if fb.verificar(cartela, sorteados) == 6:
                contador += 1
        
        if contador == 0:
            print("Nenhum Vencedor!")
        else:
            # fb.limpar()
            print("\nSorteio Finalizado Cartelas Vencedoras: \n")
            for cartela in cartelas:
                if fb.verificar(cartela, sorteados) == 6:
                    print(f"\033[32m{cartela}\033[0;0m  {fb.verificar(cartela, sorteados)}")
        print("\n\033[35mNumeros Sorteados:\033[0;0m \033[33m{}\033[0;0m".format(sorteados))
    input("Aperte <Enter> para Continuar!")
    