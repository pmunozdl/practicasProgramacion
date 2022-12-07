import unittest
import src.kataDNI
from src.kataDNI import longitud_dni
from src.kataDNI import dniLetra
from src.kataDNI import dniSuma
from src.kataDNI import nie 

class test_kataDNI(unittest.TestCase):
    #1
    def test_9_cifras(self):
        dni = "191919191" 
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
    #2
    def test_9_cifras_y_letras(self):
        dni = "F98I01Q11"
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
    #3
    def test_8_cifras(self): 
        dni = "F98I01Q1"
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
    #4
    def test_dni_valido(self):
        dni = "12345678P"
        longitud = longitud_dni(dni)
        self.assertEqual(9,longitud)
    #5
    def test_dni_letra_invalida(self):
        dni = "12345678O"
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
    #6
    def test_dni_letra_invalida_I(self):
        dni = "12345678I"
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
    #7
    def test_dni_letra_invalida_Ñ(self):
        dni = "12345678Ñ"
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
    #8
    def test_dni_letra_invalida_U(self):
        dni = "12345678U"
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
    #9
    def test_dni_letra_invalida_(self):
        dni = "12345678U"
        longitud = longitud_dni(dni)
        self.assertEqual(ValueError,longitud)
   
    
    
    
