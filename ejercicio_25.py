# Iteration master

print("Metodo 1: for")
for i in range(1,101):
    print(i)
    
print("Metodo 2: recursividad")
def aumentar(n):
    print(n)
    if(n==100):
        return n
    else:
        aumentar(n+1)
aumentar(1)

print("Metodo 3: listas")
numeros = [_ for _ in range(1,101)]
print(numeros)

