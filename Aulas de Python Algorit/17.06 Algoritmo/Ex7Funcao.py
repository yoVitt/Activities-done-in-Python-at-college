lista = [1,2,3,3,3,8,3,4,5,100,150,30]

def media(lista):
    med=0
    for i in range(0,len(lista)):
        med += lista[i]
    return med/len(lista)


def near(lista,media):                       #"near?"
    distancia=max(lista)                     #esse "max" pega o maior valor da lista
    print(f"Valor max: {distancia}")
    for idx in range(len(lista)):
        if abs(lista[idx]-media) < distancia:
            valor = lista[idx]
            distancia=abs(lista[idx]-media)   #abs(pega o valor absoluto, ou seja, o módulo, basicamente se o número der result -10, ele pegara '10')
    return valor


print(f"Valor da média:{media(lista)}")
print(f"Valor mais próximo à media: {near(lista,media(lista))}")