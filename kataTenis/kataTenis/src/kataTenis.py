'''
class PartidaTenis:

    def __init__(self, jugador1_nombre, jugador2_nombre): #constructor
        self.jugador1_nombre = jugador1_nombre
        self.jugador2_nombre = jugador2_nombre
        self.jugador1_puntos = 0
        self.jugador2_puntos = 0
    def punto(self, jugador_nombre, puntos = 1):
        if jugador_nombre == self.jugador1_nombre:
            self.jugador1_puntos += puntos
        else:
            self.jugador2_puntos += puntos
    def score(self):
        puntos = Puntuacion(self.jugador1_puntos, self.jugador2_puntos) #llamo al método que crearé más tarde

        if puntos.cero_iguales(): #
            return "Cero iguales"
        if puntos.quince_iguales():
            return "Quince iguales"
        if puntos.treinta_iguales():
            return "Treinta iguales"
        if puntos.cuarenta_iguales(): #deuce
            return "cuarenta iguales"
        if puntos.ventaja_jugador1():
            return "Ventaja para" + self.jugador1_nombre
        if puntos.ventaja_jugador2():
            return "Ventaja para" + self.jugador2_nombre
        if puntos.gana_jugador1():
            return "Victoria para" + self.jugador1_nombre
        if puntos.gana_jugador2():
            return "Victoria para" + self.jugador2_nombre
        
        resultado = ""
        nombres_puntos = {
            0: "Cero",
            1: "Quince",
            2: "Treinta",
            3: "Cuarenta"
        }
        resultado += nombres_puntos[self.jugador1_puntos]
        resultado += "-"
        resultado += nombres_puntos[self.jugador2_puntos]
        return resultado

    
class Puntuacion:
    def __init__(self, jugador1_puntos, jugador2_puntos):
        self.jugador1_puntos = jugador1_puntos
        self.jugador2_puntos = jugador2_puntos
    
    def jugadores_empate_puntos(self):
        return self.jugador1_puntos == self.jugador2_puntos
    def un_jugador_va_ganando(self):
        return self.jugador1_puntos >= 4 or self.jugador2_puntos >= 4
    def ventaja_para_jugador1(self):
        return self.un_jugador_va_ganando() and self.jugador1_puntos - self.jugador2_puntos == 1
    def ventaja_para_jugador2(self):
        return self.un_jugador_va_ganando() and self.jugador2_puntos - self.jugador1_puntos == 1
    def gana_jugador1(self):
        return self.un_jugador_va_ganando() and self.jugador1_puntos - self.jugador2_puntos >= 2
    def gana_jugador2(self):
        return self.un_jugador_va_ganando() and self.jugador2_puntos - self.jugador1_puntos >= 2
    def empate_a_cero(self):
        return self.jugador1_puntos == self.jugador2_puntos == 0
    def empate_a_quince(self):
        return self.jugador1_puntos == self.jugador2_puntos == 1
    def empate_a_treinta(self):
        return self.jugador1_puntos == self.jugador2_puntos == 2
    def empate_a_cuarenta(self):
        return self.jugador1_puntos == self.jugador2_puntos == 3
'''

class KataTenis:
    def __init__(self, jugador1_nombre, jugador2_nombre): #constructor
        self.jugador1_nombre = jugador1_nombre
        self.jugador2_nombre = jugador2_nombre
        self.jugador1_puntos = 0
        self.jugador2_puntos = 0