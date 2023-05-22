# pede ao usuário para inserir o peso em quilogramas e a altura em metros
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

# calcula o IMC usando a fórmula IMC = peso / (altura ** 2)
imc = peso / (altura ** 2)

# determina em que categoria o usuário se encontra com base no valor do IMC
if imc < 18.5:
    categoria = "abaixo do peso"
elif imc < 25:
    categoria = "com peso normal"
elif imc < 30:
    categoria = "com sobrepeso"
elif imc < 35:
    categoria = "obeso grau I"
elif imc < 40:
    categoria = "obeso grau II"
else:
    categoria = "obeso grau III"

# exibe o valor do IMC e a categoria correspondente na tela
print("Seu IMC é:", imc)
print("Você está", categoria)
