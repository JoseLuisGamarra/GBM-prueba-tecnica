import unittest
from ejercicio3.script import min_saltos

class TestMinSaltos(unittest.TestCase):

  def test_caso_simple(self):
    x = 4
    k = 2
    saltos_esperados = 3
    saltos_obtenidos = min_saltos(x, k)
    self.assertEqual(saltos_esperados, saltos_obtenidos)

  def test_caso_base(self):
    x = 1
    k = 10
    saltos_esperados = 1
    saltos_obtenidos = min_saltos(x, k)
    self.assertEqual(saltos_esperados, saltos_obtenidos)

  def test_saltos_maximos(self):
    x = 10
    k = 1
    saltos_esperados = 10
    saltos_obtenidos = min_saltos(x, k)
    self.assertEqual(saltos_esperados, saltos_obtenidos)

  def test_rango_intermedio(self):
    x = 7
    k = 3
    saltos_esperados = 4
    saltos_obtenidos = min_saltos(x, k)
    self.assertEqual(saltos_esperados, saltos_obtenidos)

if __name__ == "__main__":
    unittest.main()