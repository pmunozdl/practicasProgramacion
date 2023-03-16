class kataBolos:

    def bowling_score (self, frames):
        score = 0
        frames = frames.replace(" ", "")
        frames = frames.replace("-", "0")
        lista = self.numeroRondas(frames) #cargo la función para obtener la lista de las diez tiradas
        print(lista)
        if (len(lista)) == 10: #tiene que haber 10 rondas
            for e in range(len(lista)):
                print("elemento", e, lista[e])
                print(lista)
                if lista[e][0] == "X":
                    if e < 9:
                        if lista [e+1][0] == "X":
                            if lista [e+2][0] == "X":
                                score += 10 + self.frame_value(lista[e+1]) + self.frame_value(lista[e+2])
                            elif lista [e+2][0] != "X":
                                score += 10 + self.frame_value(lista[e+1])+ self.frame_value(lista[e+2][0])
                        elif lista[e+1][1] == "/":
                            score += 20
                            print("pleno y después semipleno",score)
                        else:
                            score += 10 + self.frame_value(lista [e+1][0]) + self.frame_value(lista[e+1][1])
                            print("pleno normal",score)
                    elif e == 9:
                        if lista[9][0] == "X":
                            if lista [9][2] == "/":
                                score += 20
                                print("pleno y semipleno en ultima ronda",score)
                            elif lista [9][1] == "X":
                                score += 10
                                if lista [9][2] =="X":
                                    score += 10
                                    print("pleno pleno pleno",score)
                                else:
                                    score += 10 + self.frame_value(lista[9][1]) + self.frame_value(lista[9][2])# no se si hay que sumar las posiciones 1 y 2
                                    print("pleno pleno y casi",score)
                elif lista[e][1] == "/": #falta el semipleno al final. Falla la resta de la tirada de delante
                    if e in range(len(lista[0:9])):
                        score += 10 + self.frame_value(lista[e + 1][0])
                        print("puntuacion semipleno", score)
                        print(self.frame_value(lista[e + 1][0]))
                    elif e == 9:
                        if lista[9][1] == "/":
                            if lista[9][2] =="X":
                                score += 20
                                print("puntuación semipleno y luego pleno",score)
                            elif (lista[9][2]).isdigit() == True:
                                score += 10 + self.frame_value(lista[9][2])
                                print("semipleno y tirada normal",score)
                
                elif lista[e].isdigit() == True: #digito
                        score += int(lista[e][0])+ int (lista[e][1])  #suma los valores si no hay pleno, o semipleno
                        print("tirada normal",score)
            print("puntuación total",score)
            return score
        
    def frame_value(self, frame):
        if frame == 'X0':
            return 10
        elif frame.isdigit() == True:
             return int(frame)
        elif frame == "X":
            return 10
        return int(frame)
    def get_frames(self, frames):
        self.frames = frames
       
    def numeroRondas(self, frames):
        numerorondas = 0 #tiene que llegar a 10
        tiradas = 0
        frames = frames.replace(" ", "")
        lista = []
        for e in range(0,len(frames)): #inicio, fin y paso
                if str(frames[e]) == "X":
                    numerorondas += 1
                    lista.append(frames[e])
                    lista.append(",")
                elif str(frames[e]) == "/" or str(frames[e]) == "-" or str(e).isdigit() == True:
                    if e <= (len(frames)-1):
                        tiradas += 1
                        lista.append(frames[e])
                        
                        if tiradas % 2 == 0:
                            numerorondas += 1
                            lista.append(",")
                else:
                     raise ValueError("no vale")
        listaComas = []
        for e in range(len(lista)):
             if lista[e] == ",":
                  listaComas.append(e)
        lista.pop(listaComas[-1])
        string = ''.join(lista)
        string = string.replace("X", "X0")
        final = string.split(",",maxsplit=9)
        if len(final) > 10:
            raise ValueError ("no puede haber más de diez rondas") 
        elif len(final[9]) > 3: 
            return(final[9][0:2])
        print(final)
        return (final)
    #def restricciones(self, frames):
#hacer un método de calcular ronda, que me permita saber en qué ronda estoy 
#bowling_score("XXX429")
#restricciones a aplicar: las sumas de cada tirada no puede ser superior a 10
#plenos solo en posiciones pares. Hacer que X = X0
#semiplenos solo en posiciones impares. 
#codigo para test
# ponerlo todo en distintas funciones, quitar los self. 


#tengo que conseguir convertir el string en una lista de las distintas tiradas. Una vez tenga la lista, podré
#acceder a las distintas tiradas. Clase prueba