def invertNum(valor):
    return valor[::-1]

def contarNum(valor):
    if valor == '1':
        return 'unidade'
    
    
def organizaNum(valor):
    novo_valor = invertNum(valor)
    lista = []
    for valor in (enumerate(novo_valor)):
        lista.append(valor)
        print lista
    return lista
