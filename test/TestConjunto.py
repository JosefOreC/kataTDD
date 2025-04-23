import unittest
from random import randint
from src.logica.conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_returnNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_promedio_returnPromedio(self):
        conjunto = Conjunto([1,3,4,5])
        promedio_esperado = 13/4
        self.assertEqual(promedio_esperado, conjunto.promedio())

    def test_conjunton_promedio_returnPromedio(self):
        num_elements = randint(1,50)
        elements= [randint(1,1000)for i in range(num_elements)]
        promedio_esperado = sum(elements)/num_elements
        conjunto = Conjunto(elements)
        self.assertEqual(promedio_esperado, conjunto.promedio())