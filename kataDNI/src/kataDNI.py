
def validador(dni):
    if dni[0] == "X" or dni[0] == "Y" or dni[0] == "Z":
        dni_nie = nie(dni) 
        valido = dni_valido(dni_nie)
        return dniLetra(valido)
      
    elif dni[0].isdigit():
        valido = dni_valido(dni)
        if valido == dni:
            return dniLetra(valido)
        else: 
            return ValueError
    else:
        return ValueError

        

def dni_valido(dni):
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
                        return dni
                else:
                    return ValueError
            else: 
                return ValueError 
        else:
            return ValueError

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
            if lista[0] == "X":
                lista[0] = "0"
                nie_valido = ''.join(lista)
                return nie_valido
            elif lista[0] == "Y":
                lista[0] = "1"
                nie_valido = ''.join(lista)
                return nie_valido
            elif lista[0] == "Z":
                lista[0] = "2"
                nie_valido = ''.join(lista)
                return nie_valido
            else:
                return dni
'''

def dni_valido(dni):
    longitud = len(dni)
    lista = list(dni)
    letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J", "Z","S","Q","V","H","L","C","K","E"]
    if longitud == 9:
        if dni[0:8].isdigit(): #caso para dni normal
            if dni[8].isdigit() == False:
                if dni[8] == "U" or dni[8] == "I" or dni[8] == "Ñ" or dni[8] == "O":
                    return ValueError
                else:
                    x = int(dni[0]) + int(dni[1]) + int(dni[2]) + int(dni[3]) + int(dni[4]) + int(dni[5]) + int(dni[6]) + int(dni[7]) 
        #falta hacer la suma para dni[0:8]
                    ans = x % 23
                    if (dni[8]) == letras[ans]:
                        return True
                    else:
                        return ValueError
            else:
                return ValueError
        elif dni[0] == "X" and dni[1:8].isdigit():
            lista[0] = "0"
            nie_valido = ''.join(lista)
            if nie_valido[0:8].isdigit():
                if nie_valido[8].isdigit() == False:
                    if nie_valido[8] == "U" or nie_valido[8] == "I" or nie_valido[8] == "Ñ" or nie_valido[8] == "O":
                        return ValueError
                    else:
                        x = int(nie_valido[0]) + int(nie_valido[1]) + int(nie_valido[2]) + int(nie_valido[3]) + int(nie_valido[4]) + int(nie_valido[5]) + int(nie_valido[6]) + int(nie_valido[7]) 
                        #falta hacer la suma para dni[0:8]
                        ans = x % 23
                        if (nie_valido[8]) == letras[ans]:
                            return True
                        else:
                            return ValueError
                else:
                    return ValueError
            else:
                    return ValueError
        elif dni[0] == "Y" and dni[1:8].isdigit():
            lista[0] = "1"
            nie_valido = ''.join(lista)
            if nie_valido[0:8].isdigit():
                if nie_valido[8].isdigit() == False:
                    if nie_valido[8] == "U" or nie_valido[8] == "I" or nie_valido[8] == "Ñ" or nie_valido[8] == "O":
                        return ValueError
                    else:
                        x = int(nie_valido[0]) + int(nie_valido[1]) + int(nie_valido[2]) + int(nie_valido[3]) + int(nie_valido[4]) + int(nie_valido[5]) + int(nie_valido[6]) + int(nie_valido[7]) 
                        #falta hacer la suma para dni[0:8]
                        ans = x % 23
                        if (nie_valido[8]) == letras[ans]:
                            return True
                        else:
                            return ValueError
                else:
                    return ValueError
            else:
                return ValueError
        elif dni[0] == "Z" and dni[1:8].isdigit():
            lista[0] = "2"
            nie_valido = ''.join(lista)
            if nie_valido[0:8].isdigit():
                if nie_valido[8].isdigit() == False:
                    if nie_valido[8] == "U" or nie_valido[8] == "I" or nie_valido[8] == "Ñ" or nie_valido[8] == "O":
                        return ValueError
                    else:
                        x = int(nie_valido[0]) + int(nie_valido[1]) + int(nie_valido[2]) + int(nie_valido[3]) + int(nie_valido[4]) + int(nie_valido[5]) + int(nie_valido[6]) + int(nie_valido[7]) 
                        #falta hacer la suma para dni[0:8]
                        ans = x % 23
                        if (nie_valido[8]) == letras[ans]:
                            return True
                        else:
                            return ValueError
                else:
                    return ValueError
            else:
                return ValueError      
        else:
            return ValueError

    else:
        return ValueError
'''