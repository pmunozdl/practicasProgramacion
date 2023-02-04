import unittest

from Bolos import PartidaBolos


class TestBolos(unittest.TestCase):

    def setUp(self):
        self.partida = PartidaBolos()
        
        return super().setUp()
    def test_creacion_partida(self):
        self.assertTrue(self.partida)

    def test_partida_mas_simple(self):
        self.rondas = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [
            0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [0, 0]}
        self.assertEqual(self.partida.resultadoPartida(self.rondas), 0)

    def test_partida_normal(self):
        self.rondas = {1: [1, 6], 2: [4, 4], 3: [2, 1], 4: [0, 0], 5: [
            0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [9, 0]}
        self.assertEqual(self.partida.resultadoPartida(self.rondas), 27)

    def test_strike(self):
        self.rondas = {1: [10, '-'], 2: [2, 1], 3: [0, 0], 4: [0, 0],
                        5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [0, 0]}
        self.assertEqual(self.partida.resultadoPartida(self.rondas), 16)

    def test_spare(self):
        self.rondas = {1: [6, 4], 2: [5, 0], 3: [0, 0], 4: [0, 0], 5: [
            0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [0, 0]}
        self.assertEqual(self.partida.resultadoPartida(self.rondas), 20)

    def test_consecutive_strikes(self):
        self.rondas = {1: [10, '-'], 2: [10, '-'], 3: [2, 0], 4: [0, 0], 5: [
            0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [0, 0]}
        self.assertEqual(self.partida.resultadoPartida(self.rondas), 36)

    def test_tenthFrame_strike(self):
        self.rondas = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [
            0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [10, 10, 10]}
        self.assertEqual(self.partida.resultadoPartida(self.rondas), 30)

    def test_tenthFrame_spare(self):
        self.rondas = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [
            0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [5, 5, 1]}
        self.assertEqual(self.partida.resultadoPartida(self.rondas), 11)

    def test_perfect_score(self):
        self.rondas = {1: [10, '-'], 2: [10, '-'], 3: [10, '-'], 4: [10, '-'], 5: [
            10, '-'], 6: [10, '-'], 7: [10, '-'], 8: [10, '-'], 9: [10, '-'], 10: [10, 10, 10]}
        self.assertEqual(self.partida.resultadoPartida(self.rondas), 300)

    def test_negative_number(self):
        self.rondas = {1: [-1, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [
            0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0], 10: [0, 0]}
        
        self.assertRaises(TypeError, self.partida.resultadoPartida, self.rondas)

if __name__ == '__main__':
    unittest.main()