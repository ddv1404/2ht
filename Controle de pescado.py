peso_peixes = float(input("Digite o peso dos peixes em quilogramas: "))

limite_peso = 50  # limite estabelecido pelo regulamento de pesca
excesso = 0  # inicialmente, não há excesso de peso
multa_por_quilo = 4.00  # valor da multa por quilo excedente
multa = 0  # inicialmente, não há multa a pagar

if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    multa = excesso * multa_por_quilo

print("Excesso de peso:", excesso)
print("Valor da multa a pagar: R$", multa)
