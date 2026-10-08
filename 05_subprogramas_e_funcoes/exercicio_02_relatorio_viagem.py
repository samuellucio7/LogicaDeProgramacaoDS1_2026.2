"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    custo=(consumo_kml*distancia_km)*preco_combustivel
    return custo
def calcular_custo_alimentacao(qtd_pessoa,dias,diaria_alimentacao):
    custo_alimentacao=(diaria_alimentacao*dias)*qtd_pessoa
    return custo_alimentacao
distancia=float(input("digite a distancia percorrida"))
consumo=float(input("digite a quantidade de combustivel consumido"))
preco_combustivel=float(input("digite o preço do combustivel"))
pessoas=int(input("digite a quantidade de pesssoas"))
dias=int(input("digite quantos dias se passaram"))
alimentacao=float(input("digite o valor da alimentação diaria"))
valor1=calcular_custo_transporte(distancia,consumo,preco_combustivel)
valor2=calcular_custo_alimentacao(pessoas,dias,alimentacao)
total=valor1=valor2
print(f"o valor do transporte foi {valor1} e o valor da alimentação foi {valor2}")