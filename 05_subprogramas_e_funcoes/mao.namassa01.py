## 🛠️ Prática do Aluno (Mão na Massa)
#Crie uma função chamada `calcular_media(nota1, nota2, nota3)` que receba três notas e retorne a média aritmética simples dessas notas.


# Teste com notas de exemplo
def calcular_media(nota1,nota2,nota3):
    media = (nota1+nota2+nota3) / 3
    return media

media1=calcular_media(9,8,10)

print(f"sua média é igual a {media1}")
