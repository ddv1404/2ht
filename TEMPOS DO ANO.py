mes = int(input("Digite o número do mês (1 a 12): "))

if mes == 1 or mes == 2 or mes == 3:
    print("A estação do ano correspondente ao mês", mes, "é Verão")
elif mes == 4 or mes == 5 or mes == 6:
    print("A estação do ano correspondente ao mês", mes, "é Outono")
elif mes == 7 or mes == 8 or mes == 9:
    print("A estação do ano correspondente ao mês", mes, "é Inverno")
elif mes == 10 or mes == 11 or mes == 12:
    print("A estação do ano correspondente ao mês", mes, "é Primavera")
else:
    print("Mês inválido. Digite um número entre 1 e 12.")
