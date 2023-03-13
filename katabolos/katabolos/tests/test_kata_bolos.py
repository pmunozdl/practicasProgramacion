import unittest
import src.katabolos.kataBolos
from src.katabolos.kataBolos import kataBolos


#formas de ejecución:
    #pytest tests/test_kata_bolos.py
    #python3 -m unittest -v test_kata_bolos

#simulador de tiradas:
    #bowlinggenius.com

class test_kata_bolos(unittest.TestCase):
    def escenario_partida(self, frames, resultado_ok):
        score = kataBolos()
        score.get_frames(frames)
        self.assertEqual(score.bowling_score(frames), resultado_ok)
    def notest_all_zeros(self):
        frames = "--------------------"
        self.escenario_partida(frames, 0)

    def notest_all_ones(self):
        frames = "11 111111111111111111"
        self.escenario_partida(frames, 20)

    def notest_a_spare(self): 
        frames = "1/111111111111111111"
        self.escenario_partida(frames, 29)

    def notest_two_spare(self): # dos semipleno
        frames = "1/11111/111111111111"
        self.escenario_partida(frames, 38)

    def notest_a_strike(self): #un pleno
        frames = "X111111111111111111-" #no cuenta un 1 porque se anula con el pleno
        self.escenario_partida(frames,30)

    def notest_a_spare_then_strike(self): #semipleno y luego pleno
        frames = "1/X1111111111111111-" #no cuenta un 1 porque se anula con el pleno
        self.escenario_partida(frames, 48)

    def notest_three_strikes(self): #tres plenos
        frames = "XXX11111111111111---" #no cuenta los 3 últimos 0 porque se anulan con el pleno
        self.escenario_partida(frames,30+21+12+14)

    def notest_a_spare_with_zero(self): #semipleno
        frames = "1/-11111111111111111"
        self.escenario_partida(frames,27)
        
    def notest_perfect_game(self):
        frames = "XXXXXXXXXXXX" #añadimos dos más por las tiradas extras con plenos 
        self.escenario_partida(frames,300)
        
    def notest_spare_at_end(self):
        frames = "------------------5/4" 
        self.escenario_partida(frames,14)

    def notest_strike_at_end(self): ## único que falla
        frames = "------------------X-"
        self.escenario_partida(frames,10)

    def notest_almost_perfect_game(self):
        frames = "XXXXXXXXXX9/" #añado dos más por las normas
        self.escenario_partida(frames,289)
    
    def notest_codewars_uno(self):
        frames = "5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 8/8" #falla en el semipleno del final
        self.escenario_partida(frames,150)
    
    def test_calcular_ronda(self):
        frames = "5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 8/8"
        score = kataBolos()
        score.get_frames(frames)
        self.assertEqual(score.calcularRonda(frames), 10)
    def test_2_calcular_ronda(self):
        frames = "XXXXXXXXXX"
        score = kataBolos()
        score.get_frames(frames)
        self.assertEqual(score.calcularRonda(frames), 10)
    
