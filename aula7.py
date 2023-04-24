#Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom,
#  considerando 10% do valor da conta.

def gorjeta(valor):
    resultado=valor*10/100
    return resultado 
valor=int(input())    
print(gorjeta(valor))    
