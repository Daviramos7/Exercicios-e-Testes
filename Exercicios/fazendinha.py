#Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.

import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)

    def __str__(self):
        return f"{self.nome}: fome={self.fome}, tédio:{self.tedio}"
    
    def alimentar(self):
        self.fome -= 1
        if self.fome < 0:
            self.fome = 0
        print(f"{self.fome} foi alimentado!")

    def brincar(self):
        self.tedio -= 1
        if self.tedio < 0:
            self.tedio = 0
        print(f"{self.nome} brincou e está mais feliz!")

    def ouvir(self):
        print(f"{self.nome} diz: 'Oi, estou aqui!'")

def main():
    fazenda = [
        Bichinho("Boris"),
        Bichinho("Fifi"),
        Bichinho("Rex"),
        Bichinho("Ralph"),
    ]

    while True:
        print("\n=== Bem-vindo à Fazenda dos Bichinhos! ===")
        print("1 - Alimentar todos os bichinhos")
        print("2 - Brincar com todos os bichinhos")
        print("3 - Ouvir todos os bichinhos")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            for bichinho in fazenda:
                bichinho.alimentar()
        elif opcao == "2":
            for bichinho in fazenda:
                bichinho.brincar()
        elif opcao == "3":
            for bichinho in fazenda:
                bichinho.ouvir()
        elif opcao == "4":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

        print("\nEstado atual da fazenda:")
        for bichinho in fazenda:
            print(bichinho)
        
if __name__ == "__main__":
    main