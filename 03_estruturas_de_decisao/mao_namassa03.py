# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))

# Desenvolva a estrutura de seleção aqui

#Opção 1: Consultar livro
#Opção 2: Realizar empréstimo
#Opção 3: Devolver livro
#Qualquer outra opção: Mensagem de "Opção Não Encontrada".


if opcao ==1:
    print("consultar livro")
elif opcao ==2:
    print("realizar emprestimo")
elif opcao == 3:
    print("devolver livro")
else:
    print("opção não encontrada")
