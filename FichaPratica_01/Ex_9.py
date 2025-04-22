

numero1 = int (input("DIGITE O PRIMEIRO NUMERO: "))
numero2 = int (input("DIGITE O SEGUNDO NUMERO: "))
numero3 = int (input("DIGITE O TERCEIRO NUMERO: "))


if numero1 < numero2 and numero3:
    menor = numero1
    print("O NUMERO É: ", menor)
elif numero2 < numero1 and numero2 < numero3 :
    menor = numero2
    print ("O NUMERO MENOR É: ", menor )
else:
    menor = numero3 
    print ("O NUMERO MENOR É ", menor)