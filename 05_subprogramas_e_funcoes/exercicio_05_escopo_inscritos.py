"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
total_de_inscritos=0 
def inscrever_alunos(quantidade):
    global total_de_escritos
    print(f"a quantidade de inscritos antes era de {total_de_inscritos} e agora é de {quantidade}")
quantidade=int(input("digite a quantidade de inscritos novos"))
inscrever_alunos (quantidade)