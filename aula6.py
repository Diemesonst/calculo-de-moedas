#Crie uma função que permita contar o número de vezes que aparece uma letr
def string(letra,palavra):
    contador=0
    for l in palavra:
         if letra==l:
            contador+=1
    return contador        
print(string('p','paralelepipedo'))       