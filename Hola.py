karen_vanessa_gonzalez= True 

def hola(value):
    global karen_vanessa_gonzalez
    karen_vanessa_gonzalez=value
    print(karen_vanessa_gonzalez)
    return "Andres Quintero Te AMOOOOOOOOOOOOOOO" #siempre está en la función o en el método, y tambien es lo ultimo

karen_vanessa_gonzalez= False
salida=hola(value=True)
print(salida)
