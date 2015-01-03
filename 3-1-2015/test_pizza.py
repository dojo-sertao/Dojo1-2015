# -*- coding;UTF-8 -*-
import unittest
from pizza import inferir
from dicionarios import *


class Test_pizza(unittest.TestCase):

    def test_se_pizza_margerita(self):
        self.maxDiff = None
        lista_nomes = ["Renato", "Lenon", "Renata", "Luca"]
        lista_nomes.sort()
        self.assertEqual(
            inferir('Marguerita'), lista_nomes)

    def test_se_pizza_4queijos(self):
        self.maxDiff = None
        lista_nomes = ["Renato", "Lenon", "Renata", "Luca", "Tino"]
        lista_nomes.sort()
        self.assertEqual(
            inferir('Quatro_queijos'), lista_nomes)

    def test_se_pizza_Escarola(self):
        self.maxDiff = None
        lista_nomes =  ["Renato", "Luca"]
        lista_nomes.sort()
        self.assertEqual(inferir('Escarola'), lista_nomes)

    def test_se_pizza_Portuguesa(self):
        self.maxDiff = None
        lista_nomes = ["Renato", "Luca", "Marcelo", "Washington", "Tino"]
        lista_nomes.sort()
        self.assertEqual(
            inferir('Portuguesa'), lista_nomes)

if __name__ == "__main__":
    unittest.main()
