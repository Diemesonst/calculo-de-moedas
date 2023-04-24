#Crie uma função que, ao receber um número inteiro.
#retorna se um número é par ou ímpar utilizando **kwargs
def decorador(function):
    def conhecendo(*args,**kwargs):
        function(*args,**kwargs)
    return conhecendo

@decorador
def verifica(n): 
    if n % 2==0:
        print('Par')
    else:
        print('Impar')
verifica(2)
        
