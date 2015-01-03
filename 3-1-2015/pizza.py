# -*- coding;UTF-8 -*-
from dicionarios import pessoas


def inferir(nome_pizza):

    result = []
    for pessoa in pessoas:
        if pessoa[nome_pizza] >= 3:
            result.append(pessoa["nome"])
    result.sort()
    return result
