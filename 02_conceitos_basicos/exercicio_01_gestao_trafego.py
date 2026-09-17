"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_investido=float(input("digite o valor investido"))
numero_de_clientes=int(input("digite a quantidade de cliques"))
custo_medio_por_cliques=((valor_investido + numero_de_clientes)/2)
print(custo_medio_por_cliques)