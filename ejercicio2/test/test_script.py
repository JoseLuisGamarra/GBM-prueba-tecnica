import unittest
from ejercicio2.script import calcular_puntos, encontrar_campeones

class TestEncontrarCampeones(unittest.TestCase):

    def test_calcular_puntos_caso_simple(self):
        resultado = [1, 2, 3]
        sistema_puntuacion = [3, 2, 1]
        puntos_esperados = 6
        #puntos_obtenidos = calcular_puntos(resultado, sistema_puntuacion)
        #self.assertEqual(puntos_esperados, puntos_obtenidos)

    def test_calcular_puntos_caso_empate(self):
        resultado = [1, 2, 3]
        sistema_puntuacion = [3, 2, 3]
        puntos_esperados = 7
        #puntos_obtenidos = calcular_puntos(resultado, sistema_puntuacion)
        #self.assertEqual(puntos_esperados, puntos_obtenidos)

    def test_encontrar_campeones_caso_simple(self):
        resultados = [[1, 2, 3], [2, 1, 3]]
        sistemas_puntuacion = [[3, 2, 1], [2, 3, 1]]
        campeones_esperados = "1 2"
        #campeones_obtenidos = encontrar_campeones(resultados, sistemas_puntuacion)
        #self.assertEqual(campeones_esperados, campeones_obtenidos)

    def test_encontrar_campeones_caso_empate(self):
        resultados = [[1, 2, 3], [2, 1, 3], [3, 2, 1]]
        sistemas_puntuacion = [[3, 2, 1], [2, 3, 1]]
        campeones_esperados = "1 2 3"
        #campeones_obtenidos = encontrar_campeones(resultados, sistemas_puntuacion)
        #self.assertEqual(campeones_esperados, campeones_obtenidos)

if __name__ == "__main__":
    unittest.main()
