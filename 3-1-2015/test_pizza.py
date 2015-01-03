import unittest 
from pizza import inferir
from dicionarios import *

class Test_pizza(unittest.TestCase):

	def test_se_pizza_margerita(self):
		self.assertEqual(inferir('Marguerita'),[Renato, Lenon, Renata, Luca])	



if __name__ == "__main__":
	unittest.main()


