#lo ejecuto con python -m unitest -v test_katabolos
import unittest

class TestBolos(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(2+2, 4)



if __name__ == '__main__':
    unittest.main(verbosity=3) #yo creo que es true pero no se que hace este hombre