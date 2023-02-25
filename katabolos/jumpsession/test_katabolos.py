#lo ejecuto con python3 -m unittest -v test_katabolos
import unittest
from katabolos import Partida
class TestBolos(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(2+2, 4)
    def test_longitud_partidas(self):
        p = Partida()
        l = p.rondas
        self.assertEqual(len(l), 10) #depende de la longitud que le ponga, en teoria tiene que ser dias
    def test_primer_triangulo(self):
        p = Partida()
        rondas = [(2,5)] * 10
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), 70)
    def test_segundo_triangulo(self):
        p = Partida()
        rondas = [(0,0)] * 10
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), 0)
    def test_tercer_triangulo(self):
        p = Partida()
        rondas = [(2,2)] * 10
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), 40)
    def test_mi_primer_pleno(self):
        p = Partida()
        rondas = [(10,0), (2,3), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), 15+5)
    def test_mi_segundo_pleno(self):
        p = Partida()
        rondas = [(10,0), (1,2), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), 13+3) 
    def test_dos_strikes_seguidos(self):
        p = Partida()
        rondas = [(10,0), (10,0), (5,3), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), 25+18+8)
    def test_dos_strikes_separados(self):
        p = Partida()
        rondas = [(10,0), (10,0), (2,4), (1,6), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), 22+16+6+7)
    def test_strike_al_final(self):
        p = Partida()
        rondas = [(0,0)] * 9 + [(10,0)] + [(2,5)]
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), 17)
    def escenario_partida(self, rondas, resultado_ok):
        p = Partida()
        p.te_paso_las_rondas(rondas)
        self.assertEqual(p.resultado(), resultado_ok)
    def test_partida_de_mierda(self):
        rondas = [(0,0)] * 10
        self.escenario_partida(rondas, 0) #hacer asi con todos


if __name__ == '__main__':
    unittest.main(verbosity=3) #yo creo que es true pero no se que hace este hombre.
    #creo que lo pone a 3 para que no funcione, porque ya pone el -v al ejecutar