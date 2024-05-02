import random

def sortear_numeros():
    
    numeros = input("Digite os números separados por espaços: ").split()
    
    
    numeros = [int(num) for num in numeros if num.isdigit()]
    
    if not numeros:
        print("Nenhum número válido foi fornecido.")
        return
    
    
    try:
        quantidade = int(input("Quantos números você deseja sortear? "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")
        return
    
    if quantidade <= 0:
        print("A quantidade de números a sortear deve ser maior que zero.")
        return
    
    if quantidade > len(numeros):
        print("A quantidade solicitada é maior do que o número de números fornecidos.")
        return
    
    
    numeros_sorteados = random.sample(numeros, quantidade)
    print(f"Números sorteados ({quantidade}):", numeros_sorteados)


sortear_numeros()
