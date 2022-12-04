import unittest
import src.kataDNI
from src.kataDNI import longitud_DNI

class test_kataDNI(unittest.TestCase):
    def test_9_cifras(self):
        dni = "1919191919" #diez cifras
        longitud = longitud_DNI(dni)
        self.assertEqual(9,longitud)