# pede ao usuário para inserir o ano de nascimento e o ano atual
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# calcula a idade da pessoa em 2099
idade_2099 = 2099 - ano_nascimento

# exibe a idade da pessoa em 2099 na tela
print("A pessoa terá", idade_2099, "anos em 2099.")
