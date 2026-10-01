"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
soma=0
quantidade=0
for i in range(6):
    valor=float(input("digite o numero: "))

if valor > 0:
    soma += valor
    quantidade+=1

media = soma/quantidade
print(f"quantidade de positivos: {quantidade}")
print (f"media dos positivos: {media:.1f}")