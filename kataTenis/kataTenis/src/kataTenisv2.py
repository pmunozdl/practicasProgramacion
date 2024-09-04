class puntuacion:
    NADA: str = "0"
    QUINCE: str = "15"
    TREINTA: str = "30"
    CUARENTA: str = "40"
    IGUALES: str = "IGUALES"
    VENTAJA: str = "VENTAJA"
    PUNTO: str = "PUNTO"

class juego:
    def __init__(self) -> None:
        self.puntuacion1: int = 0
        self.puntuacion2: int = 0
        self.diferencia: int = 0
        self.muestraPuntuacion1: str = puntuacion.ZERO
        self.muestraPuntuacion2: str = puntuacion.ZERO
        self.iguales: bool = False

    def get_muestraPuntuacion(self):
        return [self.muestraPuntuacion1, self.muestraPuntuacion2]
    def puntos(self,puntos1,puntos2):
        if puntos1 < 0 or puntos2 < 0:
            raise ValueError("Los puntos deben ser positivos")
        self.puntuacion1 += puntos1 
        self.puntuacion2 += puntos2
        self.diferencia = abs(self.puntuacion1 - self.puntuacion2)

        if self.puntuacion1 >= 3 and self.puntuacion2 >= 3:
            self.iguales = True

        if self.iguales and self.diferencia > 2:
            raise ValueError(
                "Points difference must be inferior or equal to 2 when deuce activated"
            )

        if (self.puntuacion1 > 4 and self.puntuacion2 < 3) or (
            self.puntuacion2 > 4 and self.puntuacion1 < 3
        ):
            raise ValueError(
                "A player's points cannot be above 4 if the other player's points is less than 3"
            )

        self.set_display_scores()
    def set_display_scores(self):

        if not self.iguales:
            if self.puntuacion1 == 1:
                self.muestraPuntuacion1 = puntuacion.QUINCE
            if self.puntuacion2 == 1:
                self.muestraPuntuacion2 = puntuacion.QUINCE

            if self.puntuacion1 == 2:
                self.muestraPuntuacion1 = puntuacion.TREINTA
            if self.puntuacion2 == 2:
                self.muestraPuntuacion2 = puntuacion.TREINTA

            if self.puntuacion1 == 3:
                self.muestraPuntuacion1 = puntuacion.CUARENTA
            if self.puntuacion2 == 3:
                self.muestraPuntuacion2 = puntuacion.CUARENTA

            if self.puntuacion1 == 4:
                self.muestraPuntuacion1 = puntuacion.PUNTO
            if self.puntuacion2 == 4:
                self.muestraPuntuacion2 = puntuacion.PUNTO

        else:
            self.muestraPuntuacion1 = puntuacion.IGUALES
            self.muestraPuntuacion2 = puntuacion.IGUALES

            Jugador1Ganando: bool = self.puntuacion1 > self.puntuacion2
            if self.diferencia == 1:
                if Jugador1Ganando:
                    self.muestraPuntuacion1 = puntuacion.VENTAJA
                else:
                    self.muestraPuntuacion2 = puntuacion.VENTAJA

            if self.diferencia == 2:
                if Jugador1Ganando:
                    self.muestraPuntuacion1 = puntuacion.PUNTO
                else:
                    self.muestraPuntuacion2 = puntuacion.PUNTO

