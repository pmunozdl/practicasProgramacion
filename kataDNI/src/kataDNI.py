

def longitud_dni(dni):
    longitud = len(dni)
    while longitud == 9:
        for i in range(9):
            try:
                isinstance(int(str(dni)[:8]),int)
                return longitud
            except:
                return ValueError
    else:
       return ValueError


