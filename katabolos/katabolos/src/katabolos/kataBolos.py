class kataBolos:

    def bowling_score (self, frames):
        score = 0
        frames = frames.replace(" ", "")
        frames = frames.replace("-", "0")
        print(frames)
        lista = self.numeroRondas(frames) #cargo la función para obtener la lista de las diez tiradas
        print(len(lista))
        if (len(lista)) == 10: #tiene que haber 10 rondas
            for e in range(len(lista)):
                print("elemento", e, lista[e])
                print(lista)
                if lista[e][0] == "X":
                    if e < 8:
                        if lista [e+1][0] == "X":
                            if lista [e+2][0] == "X":
                                score += 10 + self.frame_value(lista[e+1][0]) + self.frame_value(lista[e+2][0])
                                print("pleno", score)
                            elif lista [e+2][0] != "X":
                                score += 10 + self.frame_value(lista[e+1][0])+ self.frame_value(lista[e+2][0])
                                print("pleno", score)
                        elif lista[e+1][1] == "/":
                            score += 20
                            print("pleno y después semipleno",score)
                        else:
                            score += 10 + self.frame_value(lista [e+1][0]) + self.frame_value(lista[e+1][1])
                            print("pleno normal",score)
                    elif e == 8:
                        if lista [e+1][0] == "X":
                            if lista [e+1][1] == "X":
                                score += 10 + self.frame_value(lista[e+1][0]) + self.frame_value(lista[e+1][1])
                                print("pleno", score)
                            elif lista [e+1][1] != "X":
                                score += 10 + self.frame_value(lista[e+1][0])+ self.frame_value(lista[e+1][1])
                                print("pleno", score)
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
                                score += 20
                                if lista [9][2] =="X":
                                    score += 10
                                    print("pleno pleno pleno",score)
                                else:
                                    score +=self.frame_value(lista[9][2])# no se si hay que sumar las posiciones 1 y 2
                                    print("pleno pleno y casi",score)
                            else: 
                                score += 10 + self.frame_value(lista[9][1])
                                print("pleno simple", score)
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
        final = string.split(",",maxsplit=9)
        h = []
        if len(final) > 10:
            raise ValueError ("no puede haber más de diez rondas") 
        elif len(final[9]) > 3:
             ultimo = final[9]
             for e in range(len(ultimo)):
                 if ultimo[e] != ",":
                     h.append(ultimo[e])
                     string = ''.join(h)
                     primeros = final [0:9]
                     ultimos = string.split()
                     final = []
                     final= primeros + ultimos
        print("final", final)
        return (final)

 # mejora de código
 #tirada = "11-11-11-11-11-11-11-11-11-11"
 #for i in tirada:
    #if i == "-":
        #continue
    #return (i, end="") #para que no haga salto de linea
#resultado: 11111111111111111111
 #para ponerlo en codewars
 # def bowling_score (frames):
#         score = 0
#         frames = frames.replace(" ", "")
#         frames = frames.replace("-", "0")
#         lista = numeroRondas(frames) #cargo la función para obtener la lista de las diez tiradas
#         if (len(lista)) == 10: #tiene que haber 10 rondas
#             for e in range(len(lista)):
#                 if lista[e][0] == "X":
#                     if e < 8:
#                         if lista [e+1][0] == "X":
#                                 score += 10 + frame_value(lista[e+1][0])+ frame_value(lista[e+2][0])
#                         elif lista[e+1][1] == "/":
#                             score += 20
#                         else:
#                             score += 10 + frame_value(lista [e+1][0]) + frame_value(lista[e+1][1])
#                     elif e == 8:
#                         if lista [e+1][0] == "X":
#                             if lista [e+1][1] == "X":
#                                 score += 10 + frame_value(lista[e+1][0]) + frame_value(lista[e+1][1])
#                             elif lista [e+1][1] != "X":
#                                 score += 10 + frame_value(lista[e+1][0])+ frame_value(lista[e+1][1])
#                         elif lista[e+1][1] == "/":
#                             score += 20
#                         else:
#                             score += 10 + frame_value(lista [e+1][0]) + frame_value(lista[e+1][1])
#                     elif e == 9:
#                         if lista[9][0] == "X":
#                             if lista [9][2] == "/":
#                                 score += 20
#                             elif lista [9][1] == "X":
#                                 score += 20
#                                 if lista [9][2] =="X":
#                                     score += 10
#                                 else:
#                                     score += 10 + frame_value(lista[9][1]) + frame_value(lista[9][2])
#                             else: 
#                                 score += 10 + frame_value(lista[9][1])
#                 elif lista[e][1] == "/": 
#                     if e in range(len(lista[0:9])):
#                         score += 10 + frame_value(lista[e + 1][0])
#                     elif e == 9:
#                         if lista[9][1] == "/":
#                             if lista[9][2] =="X":
#                                 score += 20
#                             elif (lista[9][2]).isdigit() == True:
#                                 score += 10 + frame_value(lista[9][2])                
#                 elif lista[e].isdigit() == True: #digito
#                         score += int(lista[e][0])+ int (lista[e][1])  #suma los valores si no hay pleno, o semipleno
#             return score
#         else:
#             raise ValueError ("La partida tiene que tener 10 rondas")
        
# def frame_value(frame):
#         if frame.isdigit() == True:
#              return int(frame)
#         elif frame == "X":
#             return 10
#         return int(frame)
    
# def get_frames(frames):
#         frames = frames
       
# def numeroRondas(frames):
#         numerorondas = 0 #tiene que llegar a 10
#         tiradas = 0
#         frames = frames.replace(" ", "")
#         lista = []
#         for e in range(0,len(frames)): #inicio, fin y paso
#                 if str(frames[e]) == "X":
#                     numerorondas += 1
#                     lista.append(frames[e])
#                     lista.append(",")
#                 elif str(frames[e]) == "/" or str(frames[e]) == "-" or str(e).isdigit() == True:
#                     if e <= (len(frames)-1):
#                         tiradas += 1
#                         lista.append(frames[e])
#                         if tiradas % 2 == 0:
#                             numerorondas += 1
#                             lista.append(",")
#                 else:
#                      raise ValueError("no vale")
#         listaComas = []
#         for e in range(len(lista)):
#              if lista[e] == ",":
#                   listaComas.append(e)
#         lista.pop(listaComas[-1])
#         string = ''.join(lista)
#         final = string.split(",",maxsplit=9)
#         h = []
#         if len(final) > 10:
#             raise ValueError ("no puede haber más de diez rondas") 
#         elif len(final[9]) > 3:
#              ultimo = final[9]
#              for e in range(len(ultimo)):
#                  if ultimo[e] != ",":
#                      h.append(ultimo[e])
#                      string = ''.join(h)
#                      primeros = final [0:9]
#                      ultimos = string.split()
#                      final = []
#                      final= primeros + ultimos
#         return (final)