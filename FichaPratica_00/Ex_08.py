
    # Função para calcular a duração total
def calcular_duracao_total():
    # Entrada dos tempos das músicas em minutos e segundos
    minutos1 = int(input("Informe o tempo da 1ª música (minutos): "))
    segundos1 = int(input("Informe o tempo da 1ª música (segundos): "))
    
    minutos2 = int(input("Informe o tempo da 2ª música (minutos): "))
    segundos2 = int(input("Informe o tempo da 2ª música (segundos): "))
    
    minutos3 = int(input("Informe o tempo da 3ª música (minutos): "))
    segundos3 = int(input("Informe o tempo da 3ª música (segundos): "))
    
    minutos4 = int(input("Informe o tempo da 4ª música (minutos): "))
    segundos4 = int(input("Informe o tempo da 4ª música (segundos): "))
    
    minutos5 = int(input("Informe o tempo da 5ª música (minutos): "))
    segundos5 = int(input("Informe o tempo da 5ª música (segundos): "))
    
    # Calculando a soma total de minutos e segundos
    total_segundos = (segundos1 + segundos2 + segundos3 + segundos4 + segundos5)
    total_minutos = (minutos1 + minutos2 + minutos3 + minutos4 + minutos5)
    
    # Ajustando os segundos para minutos
    total_minutos += total_segundos // 60
    total_segundos = total_segundos % 60
    
    # Ajustando os minutos para horas
    horas = total_minutos // 60
    minutos = total_minutos % 60
    
    # Exibindo o tempo total no formato hh:mm:ss
    print(f"A duração total do álbum é: {horas:02}:{minutos:02}:{total_segundos:02}")

# Chamando a função para calcular a duração
calcular_duracao_total()
