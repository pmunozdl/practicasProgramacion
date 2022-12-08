
def longitud_dni(dni):
    longitud = len(dni)
    if longitud == 9:
        if dni[0:8].isdigit():
            if dni[8].isdigit() == False:
                if (dni[8] == "U"):
                    return ValueError
                elif (dni[8] == "I"):
                    return ValueError
                elif (dni[8] == "O"):
                    return ValueError
                elif (dni[8] == "Ñ"):
                    return ValueError
                else:
                    return longitud
            else:
                return ValueError
        else: 
            return ValueError 
    else:
        return ValueError
'''
def dniSuma(dni):
    letras = []
    respuesta = sum(letras[0:8])
    return respuesta
'''

def dniLetra(dni):
    letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J", "Z","S","Q","V","H","L","C","K","E"]
    rango = dni[0:8]
    if rango.isdigit():
        x = int(dni[0]) + int(dni[1]) + int(dni[2]) + int(dni[3]) + int(dni[4]) + int(dni[5]) + int(dni[6]) + int(dni[7]) 
        #falta hacer la suma para dni[0:8]
        ans = x % 23
        if (dni[8]) == letras[ans]:
            return True
        else:
            return ValueError
    else:
        return ValueError

def nie(dni):
        lista = list(dni)
        if lista[0] == "0":
            lista[0] = "X"
            nie_valido = ''.join(lista)
            return nie_valido
        elif lista[0] == "1":
            lista[0] = "Y"
            nie_valido = ''.join(lista)
            return nie_valido
        elif lista[0] == "2":
            lista[0] = "Z"
            nie_valido = ''.join(lista)
            return nie_valido
        else:
            return dni


