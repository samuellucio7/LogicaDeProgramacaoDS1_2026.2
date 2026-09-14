## 🛠️ Prática do Aluno (Mão na Massa)
#Escreva um programa que solicite ao usuário:
#1. O valor de uma conta de restaurante.
#2. A quantidade de amigos presentes na mesa para dividir a conta igualmente.

#O programa deve calcular e exibir quanto cada amigo deve pagar, formatando o valor com duas casas decimais.

valor_da_conta=float("digite o valor da conta")
numero_de_pessoas=int("digite o numero de pessoas")
valor_final=((valor_da_conta)/ (numero_de_pessoas))

print(f"preco que cada pessoa deve pagar e {valor_final: .2f}")
