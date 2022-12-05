

def longitud_dni(dni):
    longitud = len(dni)
    if longitud == 9:
        if dni[0:8].isdigit():
            if dni[8].isdigit() == False:
                return longitud
            else:
                return ValueError
        else: 
            return ValueError 
    else:
        return ValueError
        

 #isinstance(int(str(dni)[:8]),int)
 ##
 #ultimo = dni[8]
 #               if  ultimo == str:
 #                   if ultimo == "I":
  #                      return longitud == ValueError
   #                 elif ultimo == "O":
    #                    return longitud == ValueError
     #               elif ultimo == "Ñ":
      #                  return longitud == ValueError
       #             elif ultimo == "U":
        #                return longitud == ValueError
         #       else:
          #          return longitud
           # except:
            #    return ValueError
   # else:
   #     return ValueError
###