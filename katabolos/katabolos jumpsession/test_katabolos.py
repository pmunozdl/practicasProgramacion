#lo ejecuto con python -m unitest -v test_katabolos
import unittest
from katabolos import Partida
class TestBolos(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(2+2, 4)
    def test_longitud_partidas(self):
        p = Partida()
        l = []
        self.assertEqual(len(l), 10)


if __name__ == '__main__':
    unittest.main(verbosity=3) #yo creo que es true pero no se que hace este hombre.
    #creo que lo pone a 3 para que no funcione, porque ya pone el -v al ejecutar