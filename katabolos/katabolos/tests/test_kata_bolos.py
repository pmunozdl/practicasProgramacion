
import unittest
import src.katabolos.kataBolos
from src.katabolos.kataBolos import bowling_score

    

class test_kata_bolos(unittest.TestCase):
    def test_all_zeros(self):
        frames = "--------------------"
        score = bowling_score(frames)
        self.assertEqual(0,score)

    def test_all_ones(self):
        frames = "11 111111111111111111"
        score = bowling_score(frames)
        self.assertEqual(20,score)

    def test_a_spare(self): #semipleno(duda)
        frames = "1/111111111111111111"
        score = bowling_score(frames)
        self.assertEqual(29,score)

    def test_two_spare(self): # dos semipleno
        frames = "1/11111/111111111111"
        score = bowling_score(frames)
        self.assertEqual(38,score)

    def test_a_strike(self): #un pleno
        frames = "X111111111111111111-" #no cuenta un 1 porque se anula con el pleno
        score = bowling_score(frames)
        self.assertEqual(30,score)

    def test_a_spare_then_strike(self): #semipleno y luego pleno
        frames = "1/X1111111111111111-" #no cuenta un 1 porque se anula con el pleno
        score = bowling_score(frames)
        self.assertEqual(48,score)

    def test_three_strikes(self): #tres plenos
        frames = "XXX11111111111111---" #no cuenta los 3 últimos 0 porque se anulan con el pleno
        score = bowling_score(frames)
        self.assertEqual(30+21+12+14,score)

    def test_a_spare_with_zero(self): #semipleno
        frames = "1/-11111111111111111"
        score = bowling_score(frames)
        self.assertEqual(27,score)
        
    def test_perfect_game(self):
        frames = "XXXXXXXXXXXX" #añadimos dos más por las tiradas extras con plenos 
        score = bowling_score(frames)
        self.assertEqual(300,score)
        
    def test_spare_at_end(self):
        frames = "------------------5/" 
        score = bowling_score(frames)
        self.assertEqual(10,score)

    def test_strike_at_end(self): ## único que falla
        frames = "------------------X-"
        score = bowling_score(frames)
        self.assertEqual(10,score)

    def test_almost_perfect_game(self):
        frames = "XXXXXXXXXX9/" #añado dos más por las normas
        score = bowling_score(frames)
        self.assertEqual(289,score)
    
    def test_codewars_uno(self):
        frames = "5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 8/8" #falla en el semipleno del finañ
        score = bowling_score(frames)
        self.assertEqual(105, score)
    
