class Tenis:
    def __init__(self, nombreJugador1, nombreJugador2, max_sets):
        self.nombreJugador1 = nombreJugador1
        self.nombreJugador2 = nombreJugador2
        self.puntosJugador1 = 0
        self.puntosJugador2 = 0
        self.setsJugador1 = 0
        self.setsJugador2 = 0
        self.juegosJugador1 = 0
        self.juegosJugador2 = 0
        self.juegosMaximos = 6
        self.tieBreak = False
        self.max_sets = max_sets
        self.setsParaGanar = (max_sets // 2) + 1  # Número de sets necesarios para ganar el partido

    def juego(self):
        if self.tieBreak:
            return self.tie_break_juego()

        if self.puntosJugador1 >= 4 or self.puntosJugador2 >= 4:
            diferencia = self.puntosJugador1 - self.puntosJugador2
            if diferencia == 0:
                return "Iguales"
            elif diferencia == 1:
                return f"Ventaja {self.nombreJugador1}"
            elif diferencia == -1:
                return f"Ventaja {self.nombreJugador2}"
            elif diferencia >= 2:
                self.juegosJugador1 += 1
                self.reiniciarPuntos()
                return self.comprobarGanadorSet()
            elif diferencia <= -2:
                self.juegosJugador2 += 1
                self.reiniciarPuntos()
                return self.comprobarGanadorSet()
        else:
            return f"{self.descripcionPuntos(self.puntosJugador1)} - {self.descripcionPuntos(self.puntosJugador2)}"

    def descripcionPuntos(self, puntos):
        descripcion = {0: "0", 1: "15", 2: "30", 3: "40"}
        return descripcion[puntos]

    def ganaPunto(self, player_name):
        if player_name == self.nombreJugador1:
            self.puntosJugador1 += 1
        else:
            self.puntosJugador2 += 1
        return self.juego()

    def reiniciarPuntos(self):
        self.puntosJugador1 = 0
        self.puntosJugador2 = 0

    def comprobarGanadorSet(self):
        if self.juegosJugador1 == 6 and self.juegosJugador2 == 6:
            self.tieBreak = True
            return "Tie Break"
        
        if self.juegosJugador1 >= self.juegosMaximos and (self.juegosJugador1 - self.juegosJugador2) >= 2:
            self.setsJugador1 += 1
            if self.setsJugador1 > self.max_sets:
                raise ValueError(f"Se han superado el límite de {self.max_sets} sets")
            self.reiniciarJuegos()
            self.tieBreak = False
            if self.setsJugador1 >= self.setsParaGanar:
                return f"{self.nombreJugador1} gana el partido"
            return f"{self.nombreJugador1} gana el set"
        
        elif self.juegosJugador2 >= self.juegosMaximos and (self.juegosJugador2 - self.juegosJugador1) >= 2:
            self.setsJugador2 += 1
            if self.setsJugador2 > self.max_sets:
                raise ValueError(f"Se han superado el límite de {self.max_sets} sets")
            self.reiniciarJuegos()
            self.tieBreak = False
            if self.setsJugador2 >= self.setsParaGanar:
                return f"{self.nombreJugador2} gana el partido"
            return f"{self.nombreJugador2} gana el set"

        return f"Games: {self.nombreJugador1} {self.juegosJugador1} - {self.juegosJugador2} {self.nombreJugador2}"

    def tie_break_juego(self):
        if self.puntosJugador1 >= 7 or self.puntosJugador2 >= 7:
            diferencia = self.puntosJugador1 - self.puntosJugador2
            if diferencia >= 2:
                self.setsJugador1 += 1
                if self.setsJugador1 > self.max_sets:
                    raise ValueError(f"Se han superado el límite de {self.max_sets} sets")
                self.reiniciarPuntos()
                self.reiniciarJuegos()
                self.tieBreak = False
                if self.setsJugador1 >= self.setsParaGanar:
                    return f"{self.nombreJugador1} gana el partido"
                return f"{self.nombreJugador1} gana el tie break y el set"
            elif diferencia <= -2:
                self.setsJugador2 += 1
                if self.setsJugador2 > self.max_sets:
                    raise ValueError(f"Se han superado el límite de {self.max_sets} sets")
                self.reiniciarPuntos()
                self.reiniciarJuegos()
                self.tieBreak = False
                if self.setsJugador2 >= self.setsParaGanar:
                    return f"{self.nombreJugador2} gana el partido"
                return f"{self.nombreJugador2} gana el tie break y el set"
        
        return f"Tie Break: {self.puntosJugador1} - {self.puntosJugador2}"

    def reiniciarJuegos(self):
        self.juegosJugador1 = 0
        self.juegosJugador2 = 0

    def match_score(self):
        if self.tieBreak:
            puntos_display = f"Tie Break -> {self.nombreJugador1} {self.puntosJugador1} - {self.puntosJugador2} {self.nombreJugador2}"
        else:
            puntos_display = f"{self.nombreJugador1} {self.descripcionPuntos(self.puntosJugador1)} - {self.descripcionPuntos(self.puntosJugador2)} {self.nombreJugador2}"
        
        return (f"Sets: {self.nombreJugador1} {self.setsJugador1} - {self.setsJugador2} {self.nombreJugador2}, "
                f"Games: {self.nombreJugador1} {self.juegosJugador1} - {self.juegosJugador2} {self.nombreJugador2}, "
                f"Points: {puntos_display}")


# class Tenis:
#     def __init__(self, nombreJugador1, nombreJugador2):
#         self.nombreJugador1 = nombreJugador1
#         self.nombreJugador2 = nombreJugador2
#         self.puntosJugador1 = 0
#         self.puntosJugador2 = 0
#         self.setsJugador1 = 0
#         self.setsJugador2 = 0
#         self.juegosJugador1 = 0
#         self.juegosJugador2 = 0
#         self.juegosMaximos = 6
#         self.tieBreak = False

#     def juego(self):
#         if self.tieBreak:
#             return self.tie_break_juego()

#         if self.puntosJugador1 >= 4 or self.puntosJugador2 >= 4:
#             diferencia = self.puntosJugador1 - self.puntosJugador2
#             if diferencia == 0:
#                 return "Iguales"
#             elif diferencia == 1:
#                 return f"Ventaja {self.nombreJugador1}"
#             elif diferencia == -1:
#                 return f"Ventaja {self.nombreJugador2}"
#             elif diferencia >= 2:
#                 self.juegosJugador1 += 1
#                 self.reiniciarPuntos()
#                 return self.comprobarGanadorSet()
#             elif diferencia <= -2:
#                 self.juegosJugador2 += 1
#                 self.reiniciarPuntos()
#                 return self.comprobarGanadorSet()
#         else:
#             return f"{self.descripcionPuntos(self.puntosJugador1)} - {self.descripcionPuntos(self.puntosJugador2)}"

#     def descripcionPuntos(self, puntos):
#         descripcion = {0: "0", 1: "15", 2: "30", 3: "40"}
#         return descripcion[puntos]

#     def ganaPunto(self, player_name):
#         if player_name == self.nombreJugador1:
#             self.puntosJugador1 += 1
#         else:
#             self.puntosJugador2 += 1
#         return self.juego()

#     def reiniciarPuntos(self):
#         self.puntosJugador1 = 0
#         self.puntosJugador2 = 0

#     def comprobarGanadorSet(self):
#         if self.juegosJugador1 == 6 and self.juegosJugador2 == 6:
#             self.tieBreak = True
#             return "Tie Break"
        
#         if self.juegosJugador1 >= self.juegosMaximos and (self.juegosJugador1 - self.juegosJugador2) >= 2:
#             self.setsJugador1 += 1
#             self.reiniciarJuegos()
#             self.tieBreak = False
#             return f"{self.nombreJugador1} gana el set"
#         elif self.juegosJugador2 >= self.juegosMaximos and (self.juegosJugador2 - self.juegosJugador1) >= 2:
#             self.setsJugador2 += 1
#             self.reiniciarJuegos()
#             self.tieBreak = False
#             return f"{self.nombreJugador2} gana el set"

#         return f"Games: {self.nombreJugador1} {self.juegosJugador1} - {self.juegosJugador2} {self.nombreJugador2}"

#     def tie_break_juego(self):
#         # Lógica de puntuación para el tie break
#         if self.puntosJugador1 >= 7 or self.puntosJugador2 >= 7:
#             diferencia = self.puntosJugador1 - self.puntosJugador2
#             if diferencia >= 2:
#                 self.setsJugador1 += 1
#                 self.reiniciarPuntos()
#                 self.reiniciarJuegos()
#                 self.tieBreak = False
#                 return f"{self.nombreJugador1} gana el tie break y el set"
#             elif diferencia <= -2:
#                 self.setsJugador2 += 1
#                 self.reiniciarPuntos()
#                 self.reiniciarJuegos()
#                 self.tieBreak = False
#                 return f"{self.nombreJugador2} gana el tie break y el set"
        
#         return f"Tie Break: {self.puntosJugador1} - {self.puntosJugador2}"

#     def reiniciarJuegos(self):
#         self.juegosJugador1 = 0
#         self.juegosJugador2 = 0

#     def match_score(self):
#         if self.tieBreak:
#             puntos_display = f"Tie Break -> {self.nombreJugador1} {self.puntosJugador1} - {self.puntosJugador2} {self.nombreJugador2}"
#         else:
#             puntos_display = f"{self.nombreJugador1} {self.descripcionPuntos(self.puntosJugador1)} - {self.descripcionPuntos(self.puntosJugador2)} {self.nombreJugador2}"
        
#         return (f"Sets: {self.nombreJugador1} {self.setsJugador1} - {self.setsJugador2} {self.nombreJugador2}, "
#                 f"Games: {self.nombreJugador1} {self.juegosJugador1} - {self.juegosJugador2} {self.nombreJugador2}, "
#                 f"Points: {puntos_display}")

