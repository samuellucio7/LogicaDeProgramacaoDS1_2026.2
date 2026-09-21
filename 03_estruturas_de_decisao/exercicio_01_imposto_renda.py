"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario=float(input('digite seu salário'))
if 0< salario <=2000:
    print(f"isento")
elif 2000<salario <=3000:
    taxa1=salario*0.08
    salario_taxa1= salario-taxa1
    print(f"a sua taxa é R${taxa1: .2f}")
elif 3000<salario<=4500:
    taxa1=salario*0.08
    taxa2=salario*0.18
    taxa_geral= taxa1+taxa2
    print(f"a sua taxa é R${taxa_geral: .2f}")
elif 4500<salario:
    taxa1=salario*0.08
    taxa2=salario*0.18
    taxa3=salario*0.28
    taxa_geral2=taxa1+taxa2+taxa3
    print(f"a sua taxa é R${taxa_geral2: .2f}")
    