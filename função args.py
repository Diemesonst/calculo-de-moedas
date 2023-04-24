#rie uma função de somatório que some todos os números que a função
#  receber (usando *args)
def somatorio(*args):
    soma=0
    for i in args:
        soma = soma + i
    return soma
resultado=somatorio(5,10,5,10,7)
print(resultado)        


