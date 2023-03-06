# class kataBolos:

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

def bowling_score (frames):
        score = 0
        frames = frames.replace(" ", "")
        size = len(frames)
        if size <= 20:
            for e in frames:
                posicion = frames.index("/")
                print(posicion)
                if e == "/": #falta el semipleno al final. Falla la resta de la tirada de delante
                    if posicion < 19:
                        score += 10 + frame_value(frames[posicion + 1]) - frame_value(frames[posicion - 1])
                    elif posicion == 19:
                        score += 10 - frame_value(frames[posicion- 1])
                elif e == "X":
                    pass #método del pleno
                elif e == "-":
                    score = score
                else: 
                   score += int(e) #suma los valores si no hay pleno, o semipleno
            print (score)
            return score
        elif size > 20 and frames[19] == "X": #caso del final
            pass #poner que se añade un hueco más para ajustar a 20
        else:
            raise TypeError ("no existe esa tirada")
        
def frame_value(frame):
        if frame == 'X':
            return 10
        if frame == '-':
            return 0
        return int(frame)
bowling_score("3/0/4/8")
#restricciones a aplicar: las sumas de cada tirada no puede ser superior a 10
