# -*- coding;UTF-8 -*-
import unittest 
from pizza import inferir
from dicionarios import *

class Test_pizza(unittest.TestCase):

	def test_se_pizza_margerita(self):
		self.maxDiff = None
		self.assertEqual(inferir('Marguerita'),["Renato", "Lenon", "Renata", "Luca"])	

	def test_se_pizza_4queijos(self):
		self.maxDiff = None
		self.assertEqual(inferir('Quatro_queijos'),["Renato", "Lenon", "Renata", "Luca", "Tino"])

if __name__ == "__main__":

	unittest.main()


