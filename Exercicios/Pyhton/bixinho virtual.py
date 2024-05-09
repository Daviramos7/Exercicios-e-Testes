import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def mostrar_porta_escondida(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}"

    def alimentar(self, quantidade_comida):      
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):       
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):       
        if self.fome == 0 and self.tedio == 0:
            return "Muito feliz!"
        elif self.fome == 0 or self.tedio == 0:
            return "Feliz"
        elif self.fome > 75 or self.tedio > 75:
            return "Zangado"
        elif self.fome > 50 or self.tedio > 50:
            return "Com sono"
        else:
            return "Normal"


# Função principal para interagir com o bichinho virtual
def main():
    nome_bichinho = input("Digite o nome do seu bichinho virtual: ")
    bichinho = BichinhoVirtual(nome_bichinho)
    while True:
        print("\nEscolha uma ação:")
        print("1 - Alimentar o bichinho")
        print("2 - Brincar com o bichinho")
        print("3 - Ver humor do bichinho")
        print("4 - Opção secreta: Mostrar atributos do bichinho")
        print("0 - Sair")

        escolha = input("Digite o número da ação desejada: ")

        if escolha == "1":
            quantidade_comida = int(input("Quantidade de comida para dar ao bichinho: "))
            bichinho.alimentar(quantidade_comida)
            print(f"{bichinho.nome} foi alimentado!")
        elif escolha == "2":
            tempo_brincadeira = int(input("Tempo de brincadeira com o bichinho (em minutos): "))
            bichinho.brincar(tempo_brincadeira)
            print(f"{bichinho.nome} brincou!")
        elif escolha == "3":
            print(f"{bichinho.nome} está {bichinho.humor()}")
        elif escolha == "4":
            print(bichinho.mostrar_porta_escondida())
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()
