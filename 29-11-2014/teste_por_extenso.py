import unittest
from por_extenso import *



class testa_Unidade(unittest.TestCase):
    def teste_unidade(self):    
        self.assertEquals(contarNum('1'),'unidade')

    def testa_inverter_valor(self):
        self.assertEquals(invertNum('123'),'321')

    def testa_unidades_de_valor_123(self):
        self.assertEquals(organizaNum('123'),[(0,'3'),(1,'2'),(2,'1')])

    def testa_unidades_de_valor_123456(self):
        self.assertEquals(organizaNum('123456'),[(0,'6'),(1,'5'),(2,'4'),(3,'3'),(4,'2'),(5,'1')])



if __name__== '__main__':
    unittest.main()
    
