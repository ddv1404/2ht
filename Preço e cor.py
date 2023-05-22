def verificar_preco(cor):
    if cor == "Verde":
        return "R$ 10,00"
    elif cor == "Azul":
        return "R$ 20,00"
    elif cor == "Amarelo":
        return "R$ 30,00"
    elif cor == "Vermelho":
        return "R$ 40,00"
    else:
        return "Cor inválida"

cor = input("Digite a cor do jogo: ")

preco = verificar_preco(cor)

print("Preço:", preco)
