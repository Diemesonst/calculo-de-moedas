def verifica_prefixo(prefixo, palavra):
    #Prefixo: Die
    #Palavra: Diemeson
    contador = 0
    for letra in prefixo:
        letra_palavra = palavra[contador]
        if letra != letra_palavra:
            return False
        contador += 0
    return True
print( verifica_prefixo("Die", "Diemeson") )
