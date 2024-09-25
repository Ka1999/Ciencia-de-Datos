#Programa que toma las tres notas de un estudiante y da la nota final 
#Primera y segunda nota valen el 30% y la tercera 40%

def calcular_notas(n1, n2, n3):
    return(n1*0.3) + (n2*0.3) + (n3*0.4)

n1 = float(input("Ingresa tu primera nota: "))
n2 = float(input("Ingresa tu segunda nota: "))
n3 = float(input("Ingresa tu tercera nota: "))
 
nota_final = calcular_notas(n1, n2, n3) #Aqui estoy llamando la función calcular nota enviando las notas

print("La nota final es...", round(nota_final, 3))