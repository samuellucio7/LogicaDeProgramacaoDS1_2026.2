
# TODO: Desenvolva o acumulador com parada no 0
soma = 0
numero=int(input("digite um numero inteiro"))
while numero !=0:
    soma= soma + numero
    print (f"errado! por favor,digite um numero inteiro diferente.")
    numero= int(input("digite um numero inteiro"))
print(f"o resultado da soma é {soma}")