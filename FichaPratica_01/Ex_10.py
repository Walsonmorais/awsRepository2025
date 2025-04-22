
numeroR1 = float(input("DIGITE 1º NUMERO: "))
numeroR2 = float(input("DIGITE 2º NUMERO: "))
operador = input("INFORMA A OPERAÇÃO DESEJADA [+]|[-]|[*]|[/]\n\n==============>  ")

soma = numeroR1 + numeroR2
sub = numeroR1 - numeroR2
multi = numeroR1 * numeroR2
div = numeroR1 / numeroR2



if operador == '+':
 print("O RESULTADO DA OPERAÇÃO É: ", soma)
elif operador == '-':
 print ("O RESULTADO DA OPERAÇÃO É ", sub)
elif operador == '*' :
 print ("O RESULTADO DA OPERAÇÃO É ", multi)
elif operador == '/':
 print ("O RESULTADO DA OPERAÇÃO É ", div)
else:
 print("OPERAÇÃO INVALIDADE, SEM RESULTADO.")