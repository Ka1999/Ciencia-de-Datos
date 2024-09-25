#Crear un programa para saber si un numero ingresado es par o impar

numero = int(input('Ingresa un número: ')) #Input es para que el usuario agregue un dato y con el int se convierte en numero entero

if numero % 2 == 0: 
    print('El número es par')
else: 
    print('El número es impar')