from os import system, name
from time import sleep


class BombaCombustivel:

    def __init__(self):
        self.__gasolina = 5.69
        self.__alcool = 6.89
        self.__tipo = None
        self.__totalContas = 0

    @property
    def gasolina(self):
        return self.__gasolina

    @gasolina.setter
    def gasolina(self, novo_valor):
        self.__gasolina = novo_valor

    @property
    def alcool(self):
        return self.__alcool

    @alcool.setter
    def alcool(self, novo_valor):
        self.__alcool = novo_valor

    @property
    def tipo(self):
        return self.__tipo

    @property
    def totalContas(self):
        return self.__totalContas

    def selecionarCombustivel(self, tipo):
        if (tipo == 1):
            self.__tipo = "Gasolina"
        elif (tipo == 2):
            self.__tipo = "Alcool"
        else:
            print("Tipo Inexistente!")

    def reajuste_combustivel(self, novo_valor):
        if (novo_valor > 0):
            if (self.__tipo == "Gasolina"):
                self.__gasolina = novo_valor
            elif (self.__tipo == "Alcool"):
                self.__alcool = novo_valor

    def abastecer(self, valor):
        if (self.__tipo == "Gasolina") and (valor >= self.__gasolina):
            self.visor(valor)
        elif (self.__tipo == "Alcool") and (valor >= self.__alcool):
            self.visor(valor)

    def visor(self, valor):

        if (self.__tipo == "Gasolina"):

            litros = int(valor//self.__gasolina)

            for litro in range(1, litros+1):
                self.limpar_tela()
                print(f"""
                    POSTO DRAKAR

                    Combustivél: {self.__tipo}
                    Preço por Litro: R${self.__gasolina}

                    Abastecendo: {litro:02d} Litro(s)
                    Total a Pagar: R$ {self.__gasolina*litro:.2f}
                """)
                sleep(1.5)
            self.__totalContas += (litros*self.__gasolina)
        elif (self.__tipo == "Alcool"):

            litros = int(valor//self.__alcool)

            for litro in range(1, litros+1):
                self.limpar_tela()
                print(f"""
                    POSTO SETTA

                    Combustivél: {self.__tipo}
                    Preço por Litro: R${self.__alcool}

                    Abastecendo: {litro:02d} Litro(s)
                    Total a Pagar: R$ {self.__alcool*litro:.2f}
                """)
                sleep(1.5)
            self.__totalContas += (litros*self.__alcool)

    def zerar_bomba(self):
        self.__totalContas = 0

    def limpar_tela(self):
        if (name == 'nt'):
            system('cls')
        else:
            system('clear')

    def __str__(self) -> str:
        return f"""
        Gasolina: R$ {self.__gasolina}
        Alcool: R$ {self.alcool}
        Total Contas: {self.__totalContas}
        """
