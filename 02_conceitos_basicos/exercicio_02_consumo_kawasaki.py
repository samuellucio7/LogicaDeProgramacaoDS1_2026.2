"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia_total=float(input("digite a distancia total"))
total_de_combustivel=float(input("digite a quantidade de combustivel total"))
consumo_medio=float((total_de_combustivel + distancia_total)/2)
print(f"o consumo médio foi{consumo_medio:.2f}km/l")
