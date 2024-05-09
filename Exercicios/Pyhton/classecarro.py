class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  
        self.combustivel = 0    

    def andar(self, distancia):
        
        combustivel_necessario = distancia / self.consumo

        
        if combustivel_necessario <= self.combustivel:
            
            self.combustivel -= combustivel_necessario
            print(f"Carro andou {distancia} km.")
        else:
            
            print("Combustível insuficiente. Não foi possível completar a viagem.")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        
        self.combustivel += litros
        print(f"Abastecido com {litros} litros de combustível. Combustível total agora: {self.combustivel} litros.")



def main():
    consumo = float(input("Informe o consumo do carro (km/l): "))
    meuCarro = Carro(consumo)

    litros_abastecidos = float(input("Quantos litros de combustível deseja abastecer? "))
    meuCarro.adicionarGasolina(litros_abastecidos)

    distancia_percorrer = float(input("Informe a distância a percorrer (km): "))
    meuCarro.andar(distancia_percorrer)

    print("Combustível restante:", meuCarro.obterGasolina(), "litros")



if __name__ == "__main__":
    main()
