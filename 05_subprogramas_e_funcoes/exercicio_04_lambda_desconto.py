"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:



calcular_desconto=lambda produto: (produto - 0.15)+produto
produto=float(input("digite o valor do seu produto:"))
desconto= produto * 0.15
total=produto-desconto
print(f"o valor do seu produto com o desconto de á vista é {total}")
