import random

def sortear_numeros(minimo, maximo, quantidade):
    numeros_disponiveis = list(range(minimo, maximo + 1))
    numeros_sorteados = []

    while len(numeros_sorteados) < quantidade:
        numero_sorteado = random.choice(numeros_disponiveis)
        numeros_sorteados.append(numero_sorteado)
        numeros_disponiveis.remove(numero_sorteado)

    return numeros_sorteados, numeros_disponiveis

def sorteio_entre_sorteados(numeros_sorteados):
    while len(numeros_sorteados) > 1:
        novo_sorteio = random.sample(numeros_sorteados, 2)
        numeros_sorteados = [novo_sorteio[0]]  

    return numeros_sorteados[0]


minimo = int(input("Digite o valor mínimo do intervalo: "))
maximo = int(input("Digite o valor máximo do intervalo: "))


quantidade = int(input("Digite a quantidade de números a serem sorteados: "))


numeros_sorteio, numeros_disponiveis = sortear_numeros(minimo, maximo, quantidade)


print("Números sorteados:", numeros_sorteio)


if len(numeros_sorteio) > 1:
    continuar_sorteando = input("Deseja sortear entre os números já sorteados até sobrar apenas um? (sim/não): ").lower() == "sim"

    if continuar_sorteando:
        numero_final = sorteio_entre_sorteados(numeros_sorteio)
        print(f"O número final sorteado é {numero_final}")
