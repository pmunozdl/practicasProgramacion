

def longitud_dni(dni):
    longitud = len(dni)
    if longitud== '9':
        print("DNI Válido")
    elif len(dni) != '9':
        print("DNI inválido. Revisa que tenga 9 cifras")
    return longitud
