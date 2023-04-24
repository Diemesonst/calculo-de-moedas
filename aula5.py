def  verificar_valor(valor):
    if valor>=0:
        return('P')
    else:
        return('N')
valor = int(input())
print(verificar_valor(valor))


