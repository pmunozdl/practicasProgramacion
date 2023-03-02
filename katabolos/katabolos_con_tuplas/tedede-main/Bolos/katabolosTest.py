import unittest
import katabolos


class MyTestCase(unittest.TestCase):

    def test_todo_Ceros(self):
        bolos = katabolos.Bolos()
        partida = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        resultado = bolos.bowling_score(partida)
        self.assertEqual(0, resultado)

    def test_puntaje_variable(self):
        bolos = katabolos.Bolos()
        partida = [(0,2), (3, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.bowling_score(partida)
        self.assertEqual(6, resultado)

    def test_guion(self):
        bolos = katabolos.Bolos()
        partida = [(10,"-"), (3, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.bowling_score(partida)
        self.assertEqual(18, resultado)

    def test_strike(self):
        bolos = katabolos.Bolos()
        partida = [(9,0), (10, "-"), (5, 4), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.bowling_score(partida)
        self.assertEqual(37, resultado)

    def test_semipleno(self):
        bolos = katabolos.Bolos()
        partida = [(9,0), (10, "-"), (5, 4), (6, 4), (4, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.bowling_score(partida)
        self.assertEqual(55, resultado)

    def test_plenos_anidados(self):
        bolos = katabolos.Bolos()
        partida = [(0,0), (10, 0), (10, 0), (6, 3), (4, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.bowling_score(partida)
        self.assertEqual(58, resultado)

if __name__ == '__main__':
    unittest.main()
