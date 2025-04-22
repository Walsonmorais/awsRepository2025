# Solicita a entrada dos dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica e exibe o menor e o maior número
if numero1 > numero2:
    maior = numero1
    menor = numero2
elif numero1 < numero2:
    maior = numero2
    menor = numero1
else:
    maior = menor = numero1  # Caso os números sejam iguais

# Exibe o maior e o menor número
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
