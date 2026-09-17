"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota_um=int(input("digite sua nota da primeira avaliação"))
nota_dois=int(input("digite a nota da sua segunda avaliação"))
nota_tres=int(input("digite a nota da sua terceira avaliação"))
nota_um_peso=int(nota_um * 2)
nota_dois_peso=int(nota_dois * 3)
nota_tres_peso=int(nota_tres * 5 )
media=float((nota_um_peso + nota_dois_peso + nota_tres_peso) / 10)
print(f"sua nota final é{media:.2f}")
