"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade=int(input("digite a sua idade"))
ingresso=100
if idade<=12:
    desconto1=ingresso*0.50
    valorfinal1=ingresso-desconto1
    print(f"o valor é {valorfinal1} e seu bilhete é infantil!")
elif idade>=60:
    melhoridade=ingresso-ingresso
    valorfinal2=melhoridade
    print(f"o valor é {valorfinal2} e seu bilhete é melhor idade!")
elif idade>=13 and idade<=59:
    integral=ingresso
    valorfinal3=integral
    print(f"seu valor é {valorfinal3} e seu bilhete é integral!")
    
    

