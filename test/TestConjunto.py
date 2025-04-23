import unittest
from src.logica.conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_returnNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_promedio_returnPromedio(self):
        conjunto = Conjunto([1,3,4,5])
        promedio_esperado = 13/4
        self.assertEqual(promedio_esperado, conjunto.promedio())