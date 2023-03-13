class kataBolos:

    # def bowling_score(self, frames):
    #     score = 0
    #     index = 0
    #     rolls = 0
    #     while index < len(frames) and rolls < 20:
    #         frames = frames.replace(" ", "")
    #         frame_score= frames[index]
    #         if frame_score == "/":
    #             score += self.spare_score(frames, index)
    #         elif frame_score == 'X':
    #             rolls = rolls + 1
    #             if index < len(frames) - 2:
    #                 score += self.strike_score(frames, index)
    #         elif frame_score != '-':
    #             score += int(frame_score)
    #         index = index + 1
    #         rolls = rolls + 1
    #     return score
    
    # def get_frames(self, frames):
    #     self.frames = frames

    # def spare_score(self, frame_scores, index):
    #     if index < 18:
    #         return 10 - self.frame_value(frame_scores[index - 1]) + self.frame_value(frame_scores[index + 1])
    #     elif index == 19:
    #         return 10 - self.frame_value(frame_scores[index - 1])

    # def strike_score(self,frame_scores, index):
    #     if frame_scores[index + 2] == '/':
    #         return 20
    #     elif index == 18:  
    #         return 10 + self.frame_value(frame_scores[index + 1])
    #     elif index == 19:
    #         return 10
    #     elif index < 18:
    #         return 10 + self.frame_value(frame_scores[index + 1]) + self.frame_value(frame_scores[index + 2])

    # def frame_value(self, frame):
    #     if frame == 'X':
    #         return 10
    #     if frame == '-':
    #         return 0
    #     return int(frame)

    def bowling_score (self, frames):
        score = 0
        frames = frames.replace(" ", "")
        size = len(frames)
        for e in frames: #poner range(size)
                if e == "/": #falta el semipleno al final. Falla la resta de la tirada de delante
                    posicion = frames.index("/")
                    if posicion < 19:
                        score += 10 + self.frame_value(frames[posicion + 1]) - self.frame_value(frames[posicion - 1])
                    elif posicion == 19:
                        if posicion + 1 =="X":
                            score += 20
                        else: 
                            score += 10 - self.frame_value(frames[posicion- 1])
                    frames = frames[posicion+1:]
                elif e == "X":
                    print(frames)
                    posicion = frames.index("X")
                    print(frames)
                    if posicion + 1 == "0" and posicion + 2 == "X":
                            score += 10 + self.frame_value(frames[posicion + 1]) + self.frame_value(frames[posicion + 2])
                    elif posicion < 19:
                        score += 10 + self.frame_value(frames[posicion + 1]) + self.frame_value(frames[posicion + 2]) 
                    elif posicion > 18:
                        if posicion + 2 == "/":
                            score += 20
                        elif posicion + 1 == "X":
                            score += 10
                            if posicion + 2 =="X":
                                score += 10
                        else:
                            score += 10
                    frames = frames[posicion+1:]
                elif e == "-":
                    score = score
                else: 
                   score += int(e) #suma los valores si no hay pleno, o semipleno
        print (score)
        return score
            # elif size > 20 and frames[19] == "X": 
            #     size = size + 2
            #     score += 10 + self.frame_value(frames[posicion + 1]) + self.frame_value(frames[posicion + 2]) 
            # elif size > 20 and frames[19] == "/": 
            #     size = size + 1
            #     score += 10 - self.frame_value(frames[posicion- 1])

        # else(para el tamaño):
        #     raise TypeError ("no existe esa tirada")
        
    def frame_value(self, frame):
        if frame == 'X':
            return 10
        if frame == '-':
            return 0
        return int(frame)
    def get_frames(self, frames):
        self.frames = frames
    #def restricciones(self, frames):

#bowling_score("XXX429")
#restricciones a aplicar: las sumas de cada tirada no puede ser superior a 10
#plenos solo en posiciones pares. Hacer que X = X0
#semiplenos solo en posiciones impares. 
#codigo para test
# ponerlo todo en distintas funciones, quitar los self. 