"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

salario=float(input("digite o salario"))
if 0< salario<=400:
    reajuste1=salario*0.15
    salario_com_ajuste1=salario+reajuste1
    print(f"seu salário é de {salario_com_ajuste1} e o reajuste foi de {reajuste1}")
elif 400<salario<=800:
    reajuste2=salario*0.12
    salario_com_ajuste2=salario+reajuste2
    print(f"seu salário é de {salario_com_ajuste2} e o reajuste foi de {reajuste2}")
elif 800< salario <=1200:
    reajuste3=salario*0.10
    salario_com_ajuste3=salario+reajuste3
    print(f"seu salário é de {salario_com_ajuste3} e o reajuste foi de {reajuste3}")
elif 1200<salario <=2000:
    reajuste4=salario*0.07
    salario_com_ajuste4=salario+reajuste4
    print(f"seu salário é de {salario_com_ajuste4} e o reajuste foi de {reajuste4}")
elif 2000>salario:
    reajuste5=salario*0.04
    salario_com_ajuste5=salario+reajuste5
    print(f"seu salário é de {salario_com_ajuste5} e o reajuste foi de {reajuste5}")


