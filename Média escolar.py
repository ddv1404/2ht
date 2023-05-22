def calcular_media(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

def verificar_situacao(media):
    if media < 4:
        return "Em processo de Aprendizagem (Reprovado)"
    elif media < 8:
        return "Recuperação"
    else:
        return "Aprovado"

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = calcular_media(nota1, nota2, nota3, nota4)
situacao = verificar_situacao(media)

print("Situação do aluno:", situacao)
