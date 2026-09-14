## 🛠️ Prática do Aluno (Mão na Massa)
#Agora é a sua vez! Crie 4 variáveis para cadastrar um novo produto no estoque de informática da escola:
#1. #`nome_produto` (texto)
#2. #`quantidade_estoque` (inteiro)
#3. `preco_unitario` (ponto flutuante)
#4. `disponivel_para_venda` (booleano)

#Em seguida, exiba o valor de cada uma e seu respectivo tipo usando `print()` e `type()`.

nome_produto= str("digite o nome do seu produto")
quantidade_no_estoque= int(input ("digite a quantidadde que tem no estoque"))
preco_unitario= float(input ("digite o preco unitario"))
disponivel_para_venda= bool (input("digite a qauntidade disponivel para venda"))

print(type(nome_produto))
print(type(quantidade_no_estoque))
print(type(preco_unitario))
print(type(disponivel_para_venda))
