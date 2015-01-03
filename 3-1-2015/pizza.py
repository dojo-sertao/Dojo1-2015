# -*- coding;UTF-8 -*-
from dicionarios import *
def inferir(nome_pizza):
	#if nome_pizza == 'Marguerita':
		#return [Renato,Lenon,Renata,Luca]
	pessoas = [Renato, Lenon, Renata, Luca, Marcelo, Washington, Tino]
	result = []
	for pessoa in pessoas: 
		if pessoa[nome_pizza]>=3:
			result.append(pessoa)
	return result