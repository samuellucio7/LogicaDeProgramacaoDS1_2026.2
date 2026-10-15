"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:


def emitir_alerta_cagece(nome_cliente,valor,vencimento):
    print(f"prezado(a) {nome_cliente},sua fatura da cagece no valor de R${valor} vence no dia {vencimento}")



nome_cliente=str(input("digite seu nome:"))
valor=float(input("digite o valr da fatura:"))
vencimento=float(input("digite a data de vencimento:"))

emitir_alerta_cagece(nome_cliente,valor,vencimento)



