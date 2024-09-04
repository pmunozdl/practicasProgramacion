import unittest
from src.kataTenisv2 import *

class TestPredicciones(unittest.TestCase):
    def test_muestraPuntosJuegos(self):
        puntosA = puntuacion.QUINCE
        puntosB = puntuacion.TREINTA
        puntos = [puntosA,puntosB] 
        self.assertEqual(["15","30"], puntos)