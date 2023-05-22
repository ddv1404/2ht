codigo = int(input("Digite o código do operário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))

valor_hora_normal = 10.00  # valor por hora normal de trabalho
valor_hora_excedente = 20.00  # valor por hora excedente de trabalho
limite_horas_normais = 50  # limite de horas normais de trabalho
salario_total = 0  # inicialmente, o salário total é zero
salario_excedente = 0  # inicialmente, o salário excedente é zero

if horas_trabalhadas > limite_horas_normais:
    horas_excedentes = horas_trabalhadas - limite_horas_normais
    salario_total = (limite_horas_normais * valor_hora_normal) + (horas_excedentes * valor_hora_excedente)
    salario_excedente = horas_excedentes * valor_hora_excedente
else:
    salario_total = horas_trabalhadas * valor_hora_normal

print("Salário total: R$", salario_total)
print("Salário excedente: R$", salario_excedente)
