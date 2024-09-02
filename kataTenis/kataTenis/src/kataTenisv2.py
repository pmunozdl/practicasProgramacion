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
    def get_muestraPuntuacion(self):
        return [self.muestraPuntuacion1, self.muestraPuntuacion2]


