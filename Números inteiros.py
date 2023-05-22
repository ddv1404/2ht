numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

menor = numero1  # Assumimos que o primeiro número é o menor inicialmente

if numero2 < menor:
    menor = numero2

if numero3 < menor:
    menor = numero3

print("O menor número é:", menor)
