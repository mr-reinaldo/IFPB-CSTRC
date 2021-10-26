#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bombaCombustivel import BombaCombustivel

bomba = BombaCombustivel()
opt = 0

while opt != 9:
    bomba.limpar_tela()
    print(f"""
    POSTO DRAKAR

    R$: {bomba.totalContas:.2f}
    Gasolina: R$ {bomba.gasolina}  Alcool: R$ {bomba.alcool}

    1 - Rajuste de Preço.
    2 - Abastercer.
    3 - Zerar Bomba.

    9 - Sair
    """)
    try:
        opt = int(input("Escolha um numero referente a opção: "))

        if (opt == 9):
            break

        elif (opt == 1):
            while opt != 0:
                bomba.limpar_tela()
                print("""
                    POSTO DRAKAR

                    1 - Gasolina.
                    2 - Alcool.

                    0 - Voltar.
                    """)
                try:
                    opt = int(input("Escolha um numero referente a opção: "))
                    if (opt == 0):
                        break
                    elif (opt == 1):
                        while True:
                            bomba.limpar_tela()
                            bomba.selecionarCombustivel(1)
                            print(f"""
                            POSTO DRAKAR - REAJUSTE DE PREÇO.

                            Combustivel Selecionado: {bomba.tipo}

                            0 - Voltar.
                            """)
                            try:
                                novo_valor = float(
                                    input(f"Novo Preço para {bomba.tipo}: "))
                                bomba.reajuste_combustivel(novo_valor)

                                if novo_valor == 0:
                                    break

                                input(
                                    "Reajuste realizado! <enter> p/ continuar")
                                break
                            except ValueError:
                                input("Favor digite um valor ex. 3.48!")
                    elif (opt == 2):
                        while True:
                            bomba.limpar_tela()
                            bomba.selecionarCombustivel(2)
                            print(f"""
                            POSTO DRAKAR - REAJUSTE DE PREÇO.

                            Combustivel Selecionado: {bomba.tipo}

                            0 - Voltar.
                            """)
                            try:
                                novo_valor = float(
                                    input(f"Novo Preço para {bomba.tipo}: "))
                                bomba.reajuste_combustivel(novo_valor)

                                if novo_valor == 0:
                                    break

                                input(
                                    "Reajuste realizado! <enter> p/ continuar")
                                break
                            except ValueError:
                                input("Favor digite um valor ex. 3.48!")
                except ValueError:
                    input("Favor digitar um numero referente a opção!")

        elif (opt == 2):
            while True:
                bomba.limpar_tela()
                print("""
                POSTO DRAKAR - ABASTECIMENTO.

                1 - Gasolina.
                2 - Alcool.

                0 - Volta
                """)
                try:
                    opt = int(input("Escolha um numero referente a opção: "))

                    if(opt == 0):
                        break
                    elif (opt == 1):
                        while True:
                            bomba.limpar_tela()
                            bomba.selecionarCombustivel(1)
                            print(f"""
                            POSTO DRAKAR - ABASTECIMENTO.
                            Combustivel Selecionado: {bomba.tipo}\n

                            0 - Voltar.
                            """)
                            try:
                                valor = float(
                                    input("Valor do Abastecimento: R$ "))

                                if valor == 0:
                                    break
                                else:
                                    bomba.abastecer(valor)
                                    input("Abastecimento Realizado!")
                                    break

                            except ValueError:
                                input("Favor digite um valor ex. 3.48!")
                    elif (opt == 2):
                        while True:
                            bomba.limpar_tela()
                            bomba.selecionarCombustivel(2)
                            print(f"""
                            POSTO DRAKAR - ABASTECIMENTO.
                            Combustivel Selecionado: {bomba.tipo}\n

                            0 - Voltar.
                            """)
                            try:
                                valor = float(
                                    input("Valor do Abastecimento: R$ "))

                                if valor == 0:
                                    break
                                else:
                                    bomba.abastecer(valor)
                                    input("Abastecimento Realizado!")
                                    break

                            except ValueError:
                                input("Favor digite um valor ex. 3.48!")
                except ValueError:
                    input("Favor digitar um numero referente a opção!")
        elif(opt == 3):
            while True:
                bomba.limpar_tela()
                print(f"""
                POSTO DRAKAR - ZERAR BOMBA DE COMBUSTIVEL.
                Total do dia: {bomba.totalContas:.2f}\n

                1 - Zerar
                0 - Voltar.
                """)
                try:
                    opt = int(input("Escolha um numero referente a opção: "))

                    if opt == 0:
                        break
                    elif opt == 1:
                        bomba.zerar_bomba()
                        input("\nBomba Zerada!")

                except ValueError:
                    input("Favor digitar um numero referente a opção!")
    except ValueError:
        input("Favor digitar um numero referente a opção!")
