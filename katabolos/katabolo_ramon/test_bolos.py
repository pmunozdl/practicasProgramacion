import unittest
from Bolos import Bolos
class Test_bolos(unittest.TestCase):


    def test_calcularLaRonda1(self):
        partida = [(2,1), (3,5), (6,1), (4,2), (2,1), (3,5), (6,1), (4,2), (2,1), (3,5)]
        bolos = Bolos()
        self.assertEqual(3, bolos.calcularRonda(partida, 0))

    def test_calcularLaRonda4(self):
        partida = [(2,1), (3,5), (6,1), (4,2), (2,1), (3,5), (6,1), (4,2), (2,1), (3,5)]
        bolos = Bolos()
        self.assertEqual(6, bolos.calcularRonda(partida, 3))

    def test_calcularLaRonda6(self):
        partida = [(2,1), (3,5), (6,1), (4,2), (2,1), (3,5), (6,1), (4,2), (2,1), (3,5)]
        bolos = Bolos()
        self.assertEqual(8, bolos.calcularRonda(partida, 5))

    def test_calcularPuntuacionPartida(self):
        partida = [(2,1), (3,5), (6,1), (4,2), (2,1), (3,5), (6,1), (4,2), (2,1), (3,5)]
        bolos = Bolos()
        self.assertEqual(59, bolos.calcularPuntuacion(partida))

    def test_calcularPuntuacionPartida2(self):
        partida2 = [(3,5), (3,5), (6,1), (4,2), (2,1), (3,5), (6,1), (4,2), (2,1), (3,5)]
        bolos = Bolos()
        self.assertEqual(64, bolos.calcularPuntuacion(partida2))

    def test_calcularPuntuacionPartida3(self):
        partida3 = [(3,5), (3,5), (6,1), (4,3), (2,1), (3,5), (7,1), (4,2), (2,1), (3,5)]
        bolos = Bolos()
        self.assertEqual(66, bolos.calcularPuntuacion(partida3))

    def test_strike(self):
        partida4 = [(10,0), (5,1), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        bolos = Bolos()
        self.assertEqual(22, bolos.calcularPuntuacion(partida4))

    def test_strike_consecutivos(self):
        partida5 = [(10,0), (10,0), (5,1), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        bolos = Bolos()
        self.assertEqual(47, bolos.calcularPuntuacion(partida5))

    def test_spare(self):
        partida6 = [(8,2), (5,1), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        bolos = Bolos()
        self.assertEqual(21, bolos.calcularPuntuacion(partida6))

    def test_partidaConStrikeYSpare(self):
        partida7 = [(8,2), (5,1), (6,1), (4,2), (2,1), (3,5), (10,0), (10,0), (2,1), (6,3)]
        bolos = Bolos()
        self.assertEqual(92, bolos.calcularPuntuacion(partida7))

    def test_spare0_10(self):
        partida8 = [(5,1), (9,1), (8,2), (10,0), (0,10), (3,1), (0,0), (0,0), (0,0), (0,0)]
        bolos = Bolos()
        self.assertEqual(81, bolos.calcularPuntuacion(partida8))

    def test_partidaPerfecta(self):
        partidaPerfecta = [(10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0), (10,0)]
        bolos = Bolos()
        self.assertEqual(300, bolos.calcularPuntuacion(partidaPerfecta))

    def test_partidaExtraña(self):
         partidaExtraña = [(5,1), (9,1), (0,10), (10,0), (0,10), (0,10), (3,7), (10,0), (10,0), (1,0)]
         bolos = Bolos()
         self.assertEqual(132, bolos.calcularPuntuacion(partidaExtraña))

    def test_spareAlFinal(self):
         part = [(5,1), (9,1), (0,10), (10,0), (0,10), (0,10), (3,7), (10,0), (10,0), (9,1), (8, 2)]
         bolos = Bolos()
         self.assertEqual(174, bolos.calcularPuntuacion(part))

    if __name__ == "__main__":
        unittest.main()