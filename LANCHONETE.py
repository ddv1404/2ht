# Entrada de dados
codigo = int(input("Digite o código do lanche: "))
quantidade = int(input("Digite a quantidade: "))

# Cálculo do valor a ser pago
if codigo == 100:
    valor_total = quantidade * 1.2
    print("Valor total: R$ {:.2f}".format(valor_total))
elif codigo == 101:
    valor_total = quantidade * 1.3
    print("Valor total: R$ {:.2f}".format(valor_total))
elif codigo == 102:
    valor_total = quantidade * 1.2
    print("Valor total: R$ {:.2f}".format(valor_total))
elif codigo == 103:
    valor_total = quantidade * 1.3
    print("Valor total: R$ {:.2f}".format(valor_total))
elif codigo == 104:
    valor_total = quantidade * 1.0
    print("Valor total: R$ {:.2f}".format(valor_total))
else:
    print("Código inválido.")
