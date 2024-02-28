import unittest 
from ejercicio1.script import palindromo

class TestPalindromo(unittest.TestCase):
    def test_palindromo_true(self):
        self.assertTrue(palindromo("radar"), "palíndromo verdadero.")

    def test_palindromo_false(self):
        self.assertFalse(palindromo("hola"), "palíndromo falso.")

    def test_palindromo_empty_string(self):
        self.assertTrue(palindromo(""), "No detecta un palíndromo verdadero en una cadena vacía.")
    
   
if __name__ == 'main':
    unittest.main()
