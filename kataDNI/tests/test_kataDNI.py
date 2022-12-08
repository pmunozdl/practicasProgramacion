import unittest
import src.kataDNI
from src.kataDNI import longitud_dni
from src.kataDNI import dniLetra
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
    def test_dni_letra_invalida_O(self):
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
    def test_letra_buena(self):
        dni = "00000000T"
        bueno = dniLetra(dni)
        self.assertEqual(True,bueno)
    #10
    def test_letra_erronea(self):
        dni = "00000001P"
        bueno = dniLetra(dni)
        self.assertEqual(ValueError,bueno)
    #11
    def test_nie_valido_0(self):
        dni = "00000000T"
        bueno = nie(dni)
        self.assertEqual("X0000000T",bueno)
     #12
    def test_nie_valido_1(self):
        dni = "10000000R"
        bueno = nie(dni)
        self.assertEqual("Y0000000R",bueno)
     #13
    def test_nie_valido_2(self):
        dni = "20000000W"
        bueno = nie(dni)
        self.assertEqual("Z0000000W",bueno)
    def test_nie_caso_especial(self):
        dni = "01200000A"
        bueno = nie(dni)
        self.assertEqual("X1200000A",bueno)
        
   
    
    
    
