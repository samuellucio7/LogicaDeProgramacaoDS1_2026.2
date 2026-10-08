"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuacao_total(fase1,fase2,fase3):
    pontuacao= fase1 +  fase2 + fase3
    return pontuacao
fase1=float(input("digite a pontuação da fase 1:"))
fase2=float(input("digite a pontuação da fase 2:"))
fase3=float(input("digite a pontuação da fase 3:"))
pontuacao_total=calcular_pontuacao_total(fase1,fase2,fase3)
print(f"a pontuação da equipe é igual a {pontuacao_total}")