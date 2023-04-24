#Crie de forma recursiva uma função 
# que printe do número recebido até o zero.
  
def imprime(n):
    print(n)
    if n > 0:
     imprime(n-1)
num=10
imprime(num)

