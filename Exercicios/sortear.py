import random

def sortear_numeros():
    try:
        minimo = int(input("Digite o número mínimo do intervalo: "))
        maximo = int(input("Digite o número máximo do intervalo: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros válidos.")
        return
    
    if minimo >= maximo:
        print("O número mínimo deve ser menor que o número máximo.")
        return
    
    try:
        quantidade = int(input("Quantos números você deseja sortear? "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")
        return
    
    if quantidade <= 0:
        print("A quantidade de números a sortear deve ser maior que zero.")
        return
    
    numeros = list(range(minimo, maximo + 1))
    
    if quantidade > len(numeros):
        print("A quantidade solicitada é maior do que o número de números no intervalo especificado.")
        return
    
    numeros_sorteados = random.sample(numeros, quantidade)
    print(f"Números sorteados ({quantidade}):", numeros_sorteados)

sortear_numeros()
