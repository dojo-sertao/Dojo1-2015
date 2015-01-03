# -*- coding;UTF-8 -*-
from dicionarios import *


def inferir(nome_pizza):

    pessoas = [Renato, Lenon, Renata, Luca, Marcelo, Washington, Tino]
    result = []
    for pessoa in pessoas:
        if pessoa[nome_pizza] >= 3:
            result.append(pessoa["nome"])
    return result
