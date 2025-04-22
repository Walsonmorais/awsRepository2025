# Solicita o preço dos três produtos
preco_produto_1 = float(input("Digite o preço do primeiro produto: R$ "))
preco_produto_2 = float(input("Digite o preço do segundo produto: R$ "))
preco_produto_3 = float(input("Digite o preço do terceiro produto: R$ "))

# Calcula o valor total sem o desconto
total = preco_produto_1 + preco_produto_2 + preco_produto_3

# Aplica um desconto de 10% no valor total
desconto = total * 0.10
total_com_desconto = total - desconto

# Exibe o valor total com o desconto aplicado
print(f"O valor total sem desconto é: R$ {total:.2f}")
print(f"O valor do desconto de 10% é: R$ {desconto:.2f}")
print(f"O valor total com desconto é: R$ {total_com_desconto:.2f}")
