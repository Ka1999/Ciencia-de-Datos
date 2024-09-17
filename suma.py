
#Las funciones sirven para no repetir codigo
def suma(sumando_uno, sumando_dos):
    sumando_uno = int(sumando_uno)
    sumando_dos = int(sumando_dos)
    resultado = sumando_uno + sumando_dos
    return resultado

print(suma(sumando_uno=input(), sumando_dos=input())) 
