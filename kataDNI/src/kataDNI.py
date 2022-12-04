class kataDNI:

def longitud_DNI(a):
    longitud = 0
    if len(a)== '9':
        longitud = 9
        print("DNI válido") 
    elif len(a) != '9':
            print("DNI inválido. Revisa que tenga 9 cifras")
    return longitud