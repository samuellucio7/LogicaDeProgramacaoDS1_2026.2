# TODO: Crie o dicionário do veículo e percorra com for
marca=str(input("digite a marca do seu vrum vrum:  "))
modelo=str(input("digite o modelo do seu vrum vrum: "))
ano=str(input("digite o ano do seu vrum vrum:  "))

veiculo = {
"marca:": {marca},
"modelo:": {modelo},
"ano:": {ano},
}


# Escreva o laço for com .items()
for linha in veiculo.items():
    marca=linha[0]
    modelo=linha[1]
    ano=linha[0]
print("consultoria,",veiculo)
