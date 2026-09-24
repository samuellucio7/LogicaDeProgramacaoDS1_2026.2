"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

codigo_item=float(input("digite o codigo"))
consumido=float(input("digite a quantidade consumida"))
if codigo_item==1:
    preco_total=(consumido)*4
    print(f"valor total R${preco_total}")
elif codigo_item==2:
    preco_total=(consumido)*4.50
    print(f"valor total R${preco_total}")
elif codigo_item==3:
    preco_total=(consumido)*5
    print(f"valor total R${preco_total}")
elif codigo_item==4:
    preco_total=(consumido)*2
    print(f"valor total R${preco_total}")
elif codigo_item==5:
    preco_total=(consumido)*1.50
    print(f"valor total R${preco_total}")



