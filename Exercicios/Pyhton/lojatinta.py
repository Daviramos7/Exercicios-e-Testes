#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros; comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

def calcular_quantidade_tinta(area):
    litros_necessarios = area / 6
    litros_necessarios *= 1.1
    return litros_necessarios

def calcular_preco_comprar_apenas_latas(litros_necessarios):
    latas_necessarias = math.ceil(litros_necessarios / 18)
    preco_total = latas_necessarias * 80
    return latas_necessarias, preco_total

def calcular_preco_comprar_apenas_galoes(litros_necessarios):
    galoes_necessarios = math.ceil(litros_necessarios / 3.6)
    preco_total = galoes_necessarios * 25
    return galoes_necessarios, preco_total

def calcular_preco_misturar_latas_galoes(litros_necessarios):
    latas_inteiras = int(litros_necessarios / 18)
    litros_restantes = litros_necessarios % 18
    galoes_inteiros = math.ceil(litros_restantes / 3.6)
    preco_total = (latas_inteiras * 80) + (galoes_inteiros * 25)
    return latas_inteiras, galoes_inteiros, preco_total

area_a_pintar = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = calcular_quantidade_tinta(area_a_pintar)

latas, preco_latas = calcular_preco_comprar_apenas_latas(litros_necessarios)
galoes, preco_galoes = calcular_preco_comprar_apenas_galoes(litros_necessarios)
latas_misturadas, galoes_misturados, preco_misturado = calcular_preco_misturar_latas_galoes(litros_necessarios)

print(f"Quantidade de tinta necessária: {litros_necessarios:.2f} litros\n")

print(f"Comprando apenas latas de 18 litros:")
print(f"   - {latas} latas")
print(f"   - Preço total: R$ {preco_latas:.2f}\n")

print(f"Comprando apenas galões de 3,6 litros:")
print(f"   - {galoes} galões")
print(f"   - Preço total: R$ {preco_galoes:.2f}\n")

print(f"Misturando latas e galões para minimizar o desperdício:")
print(f"   - {latas_misturadas} latas e {galoes_misturados} galões")
print(f"   - Preço total: R$ {preco_misturado:.2f}")
