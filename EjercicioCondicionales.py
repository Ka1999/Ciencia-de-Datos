edad = int (input('Ingresa tu edad: '))

if edad >= 18: 
    print('Es mayor de edad')
elif edad >= 14 and edad <= 17: #se usa para varias opciones
    print('Es adolescente')
elif edad >= 5 and edad <= 13: #se usa para varias opciones
    print('Es niño')