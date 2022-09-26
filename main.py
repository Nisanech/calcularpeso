# Calcular nuestro peso en Marte y Neptuno

while True:
    peso_tierra = int(input('Ingresa tu peso en Kg: '))

    if peso_tierra > 0:
        while True:
            planeta = int(input('Elige 1 para Marte o 2 para Neptuno '))

            # Fórmula: (peso_tierra * gravedad_planeta) / gravedad_tierra

            if planeta == 1:
                peso_marte = (peso_tierra * 3.721) / 9.8
                print('Tu peso en Marte es: ' + str(peso_marte))
                break

            elif planeta == 2:
                peso_neptuno = (peso_tierra * 11.15) / 9.8
                print('Tu peso en Neptuno es: ' + str(peso_neptuno))
                break
            else:
                print('Elije una opción válida')
        break
