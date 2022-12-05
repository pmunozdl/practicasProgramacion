import unittest
import src.kataDNI
from src.kataDNI import longitud_dni

class test_kataDNI(unittest.TestCase):

    def test_9_cifras(self):
        dni = "191919191" 
        longitud = longitud_dni(dni)
        self.assertEqual(9,longitud)
    def test_9_cifras_y_letras(self):
        dni = "F98I01Q11"
        longitud = longitud_dni(dni)
        self.assertEqual(9,longitud)
    def test_8_cifras(self): #no deberia pasar
        dni = "F98I01Q1"
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
    
