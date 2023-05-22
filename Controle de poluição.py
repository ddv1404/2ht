indice_poluicao = float(input("Digite o índice de poluição medido: "))

grupo1 = 0.3  # índice para suspender atividades do grupo 1
grupo2 = 0.4  # índice para suspender atividades do grupo 1 e 2
grupo3 = 0.5  # índice para suspender atividades de todos os grupos

if indice_poluicao >= grupo3:
    print("Atenção: Todos os grupos devem paralisar suas atividades!")
elif indice_poluicao >= grupo2:
    print("Atenção: As indústrias do 1º e 2º grupo devem suspender suas atividades!")
elif indice_poluicao >= grupo1:
    print("Atenção: As indústrias do 1º grupo devem suspender suas atividades!")
else:
    print("Índice de poluição aceitável. Nenhuma notificação necessária.")
