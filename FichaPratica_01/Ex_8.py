


print("-----------------------SEJA BEM VINDO E DIGITE SUA NOTA----------------")

# NOTA 1 
nota1 = float(input("1º NOTA: "))
nota1 = nota1 * 0.25


# NOTA 2 
nota2 = float(input("2º NOTA: "))
nota2 = nota2 * 0.35

# NOTA 3 
nota3 = float(input("3º NOTA: "))
nota3 = nota3 * 0.40

resultadoAP ="APROVADO"
resultadoRP ="REPROVADO"

mediaFinal = (nota1 + nota2 + nota3)/ 3


if mediaFinal>=9.5 :
    print("PARABENS O SEU RESULTADO FINAL É: ", resultadoAP)

    if mediaFinal>20:
      print("COLOQUE A NOTA ADEQUADA PARA A AVALIAÇÃO")
else:
        print("INFELIZMENTE NÃO TEVE SUCESSO. O SEU RESULTADO FINAL É: ", resultadoRP)

print("A SUA NOTA FINAL É: ", mediaFinal)
print("-------------------------------------------------------------------------")
