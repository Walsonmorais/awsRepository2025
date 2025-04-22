# Solicita a entrada da posição final do piloto
posicao = int(input("Digite a posição final do piloto (1 a 8): "))

# Calcula os pontos com base na posição
if posicao == 1:
    pontos = 10
elif posicao == 2:
    pontos = 8
elif posicao == 3:
    pontos = 6
elif posicao == 4:
    pontos = 5
elif posicao == 5:
    pontos = 4
elif posicao == 6:
    pontos = 3
elif posicao == 7:
    pontos = 2
elif posicao == 8:
    pontos = 1
else:
    pontos = "NÃO GANHOU! " # Caso a posição seja maior que 8 (ou negativa)

# Exibe a quantidade de pontos que o piloto ganhou
print(f"O piloto ganhou {pontos} pontos.")
