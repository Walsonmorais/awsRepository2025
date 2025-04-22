
print ("___________________________SELECIONE A TECLA DA SUA OPCÇÃO DESEJADA_______________________\n" \
"1. CRIAR\n"
"2. ATUALIZAR\n"
"3. ELIMINAR\n"
"4. SAIR")

option = int(input("==========>   "))


if option == 1:
    print("NOME:\n"
"TELEFONE:\n"
"MORADA:\n")
elif option == 2:
    print("ATUALIZAR NOME:\n"
"ATUALIZAR TELEFONE:\n"
"ATUALIZAR MORADA:\n")
elif option == 3:
    print("O SEUS DADOS FORAM ELIMINADOS.")
elif option == 4:
    print("VOLTE SEMPRE QUE DESEJAR.")
else:
    print("ERRO: OPCÇÃO INVALIDA")

    1