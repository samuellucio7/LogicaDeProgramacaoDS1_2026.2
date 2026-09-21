# TODO: Implemente a expressão de validação
media_aluno =float(input("digite a media do aluno"))
frequencia_percentual = float(input("digite o porcentual de frequencia do aluno"))

# Crie a variável aprovado com a expressão lógica
aprovado = media_aluno>=6 and frequencia_percentual >=75
print("Status de aprovação:", aprovado)