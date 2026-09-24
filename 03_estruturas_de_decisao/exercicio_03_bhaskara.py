"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
import math
a=float(input("digite a variavel A"))
b=float(input("digite a variavel B"))
c=float(input("digite a variavel c"))
delta=b**2-4*a*c

if delta>=0:
    raizx1=(-b+math.sqrt(delta))/(2*a)
    raizx2=(-b-math.sqrt(delta))/(2*a)
    print(f"as raizes são {raizx1} e {raizx2}")
else:
    print("impossivel de calcular")