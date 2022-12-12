import unittest
from src.kataDNI import kataDNI


class test_kataDNI(unittest.TestCase):
    #1
    def test_9_cifras(self):
        dni = "191919191"
        longitud = kataDNI()
        self.assertEqual(ValueError,longitud.longitud_dni(dni))
    #2
    def test_9_cifras_y_letras(self):
        dni = "F98I01Q11"
        longitud = kataDNI()
        self.assertEqual(ValueError,longitud.longitud_dni(dni))
    #3
    def test_8_cifras(self): 
        dni = "F98I01Q1"
        longitud = kataDNI()
        self.assertEqual(ValueError,longitud.longitud_dni(dni))
    #4
    def test_kataDNI(self):
        dni = "12345678J"
        longitud = kataDNI()
        self.assertEqual(9,longitud.longitud_dni(dni))
    #5
    def test_dni_letra_invalida_O(self):
        dni = "12345678O"
        longitud = kataDNI()
        self.assertEqual(ValueError,longitud.longitud_dni(dni))
    #6
    def test_dni_letra_invalida_I(self):
        dni = "12345678I"
        longitud = kataDNI()
        self.assertEqual(ValueError,longitud.longitud_dni(dni))
    #7
    def test_dni_letra_invalida_Ñ(self):
        dni = "12345678Ñ"
        longitud = kataDNI()
        self.assertEqual(ValueError,longitud.longitud_dni(dni))
    #8
    def test_dni_letra_invalida_U(self):
        dni = "12345678U"
        longitud = kataDNI()
        self.assertEqual(ValueError,longitud.longitud_dni(dni))
    #9
    def test_letra_buena(self):
        dni = "00000000T"
        bueno = kataDNI()
        self.assertEqual(True,bueno.dniLetra(dni))
    #10
    def test_letra_erronea(self):
        dni = "00000001P"
        bueno = kataDNI()
        self.assertEqual(ValueError,bueno.dniLetra(dni))
    #11
    def test_nie_valido_0(self):
        dni = "X0000000T"
        bueno = kataDNI()
        self.assertEqual("00000000T",bueno.nie(dni))
     #12
    def test_nie_valido_1(self):
        dni = "Y0000000R"
        bueno = kataDNI()
        self.assertEqual("10000000R",bueno.nie(dni))
     #13
    def test_nie_valido_2(self):
        dni = "Z0000000W"
        bueno = kataDNI()
        self.assertEqual("20000000W",bueno.nie(dni))
    #14
    def test_nie_caso_especial(self):
        dni = "X1200000A"
        bueno = kataDNI()
        self.assertEqual("01200000A",bueno.nie(dni))
'''
 #test para métodos sin constructor
    #1
    def test_9_cifras(self):
        dni = "191919191" 
        longitud = dni_valido(dni)
        self.assertEqual(ValueError,longitud)
    #2
    def test_9_cifras_y_letras(self):
        dni = "F98I01Q11"
        longitud = dni_valido(dni)
        self.assertEqual(ValueError,longitud)
    #3
    def test_8_cifras(self): 
        dni = "F98I01Q1"
        longitud = dni_valido(dni)
        self.assertEqual(ValueError,longitud)
    #4
    def test_dni_valido(self):
        dni = "12345678J"
        longitud = dni_valido(dni)
        self.assertEqual(True,longitud)
    #5
    def test_dni_letra_invalida_O(self):
        dni = "12345678O"
        longitud = dni_valido(dni)
        self.assertEqual(ValueError,longitud)
    #6
    def test_dni_letra_invalida_I(self):
        dni = "12345678I"
        longitud = dni_valido(dni)
        self.assertEqual(ValueError,longitud)
    #7
    def test_dni_letra_invalida_Ñ(self):
        dni = "12345678Ñ"
        longitud = dni_valido(dni)
        self.assertEqual(ValueError,longitud)
    #8
    def test_dni_letra_invalida_U(self):
        dni = "12345678U"
        longitud = dni_valido(dni)
        self.assertEqual(ValueError,longitud)
    #9
    def test_letra_buena(self):
        dni = "00000000T"
        bueno = dni_valido(dni)
        self.assertEqual(True,bueno)
    #10
    def test_letra_erronea(self):
        dni = "00000001P"
        bueno = dni_valido(dni)
        self.assertEqual(ValueError,bueno)
    #11
    def test_nie_valido_0(self):
        dni = "X0000000T"
        bueno = dni_valido(dni)
        self.assertEqual(True,bueno)
     #12
    def test_nie_valido_1(self):
        dni = "Y0000000R"
        bueno = dni_valido(dni)
        self.assertEqual(True,bueno)
     #13
    def test_nie_valido_2(self):
        dni = "Z0000000W"
        bueno = dni_valido(dni)
        self.assertEqual(True,bueno)
    def test_nie_caso_especial(self):
        dni = "X1200000A"
        bueno = dni_valido(dni)
        self.assertEqual(True,bueno)
 '''       
   
    
    
    
