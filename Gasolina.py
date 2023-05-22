distancia = float(input("Digite a distância percorrida em quilômetros: "))
litros = float(input("Digite a quantidade de litros de combustível consumidos: "))
preco_gasolina = float(input("Digite o preço da gasolina por litro: "))

consumo_medio = distancia / litros
gasto_combustivel = litros * preco_gasolina

print("Consumo médio: ", consumo_medio, " km/l")
print("Gasto com combustível: R$", gasto_combustivel)
