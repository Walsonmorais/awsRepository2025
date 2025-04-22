# Solicita a entrada do salário anual
salario = float(input("Digite o salário anual: R$ "))

# Verifica a faixa de imposto e calcula o valor do imposto
if salario <= 15000:
    imposto = salario * 0.20  # 20% de imposto
elif salario <= 20000:
    imposto = salario * 0.30  # 30% de imposto
elif salario <= 25000:
    imposto = salario * 0.35  # 35% de imposto
else:
    imposto = salario * 0.40  # 40% de imposto

# Exibe o valor do imposto a ser pago
print("O imposto a ser pago é: R$ ", imposto)
