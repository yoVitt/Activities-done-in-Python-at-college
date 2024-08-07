n1=0
n2=0
resultado=0

def somar_retornando3_parametros(numero1,numero2):
    resultado=numero1+numero2
    return numero1,numero2,resultado


n1, n2, resultado= somar_retornando3_parametros(3,5)

print(f"primeiro parametro é {n1}.")
print(f"segundo parametro é {n2}.")
print(f"O resultado é {resultado}.")