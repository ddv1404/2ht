nota = float(input("Digite a nota do aluno: "))

if nota == 10:
    conceito = "Excelente"
elif 8 <= nota <= 9.9:
    conceito = "Ótimo"
elif 7 <= nota < 8:
    conceito = "Bom"
elif 5 <= nota < 7:
    conceito = "Regular"
else:
    conceito = "Insuficiente"

print(f"O aluno obteve a nota {nota} e seu conceito é {conceito}")

