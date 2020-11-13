import numpy as np

# Reading number of unknowns
n = int(input('Digite o número de nós: '))

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))
matriz = [[" " for i in range(n)] for j in range(n)]

# Reading data points
print('Digite os valores de x e f(x): ')
print("Y = f(x)")
print()
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']= '))
    y[i] = float(input( 'y['+str(i)+']= '))
    matriz[i][0] = x[i]

print()
for i in range(1, n):
    k = 0
    for j in range(i, n):
        matriz[j][i] = (matriz[j][i-1] - matriz[j-1][i-1])/(y[j] - y[k])
        k += 1

print("Ordem 0\tOrdem 1\tOrdem 2\tOrdem 3\tOrdem 4\t")
for i in range(n):
    for j in range(n):
        if(matriz[i][j] != " "): print("%.4f"%matriz[i][j], end="\t")
        else: print(" ", end="\t")
    print()

print()
for i in range(n):
    if(matriz[i][i]>=0): print(" + %.4f"%matriz[i][i], end= "")
    else: print(" - %.4f"%abs(matriz[i][i]), end= "")

    for j in range(i):
        if(y[j]>=0): print("(y-%.4f)"%y[j], end= "")
        elif(y[j]<0): print("(y+%.4f)"%abs(y[j]), end= "")

print("\n")
for i in range(n):
    if(matriz[i][i]>0):
        print(" + %.4f"%matriz[i][i], end= "")
        for j in range(i):
            if(y[j]>0): print("(y-%.4f)"%y[j], end= "")
            elif(y[j]<0): print("(y+%.4f)"%abs(y[j]), end= "")
            else: print("(y)", end= "")
    elif(matriz[i][i]<0):
        print(" - %.4f"%abs(matriz[i][i]), end= "")
        for j in range(i):
            if(y[j]>0): print("(y-%.4f)"%y[j], end= "")
            elif(y[j]<0): print("(y+%.4f)"%abs(y[j]), end= "")
            else: print("(y)", end= "")

print("\n")
erro = float(input("Calculo do Erro: "))
ordem = int(input("Ordem: "))
ap = int(input("A partir de qual linha? "))

maior = 1.0
for i in range(ap, ap+3):
    maior *= (erro-y[i])

maior = abs(maior)

dd = 0
for i in range(ordem+1, n):
    if(abs(matriz[i][ordem+1]) > dd): dd = float(abs(matriz[i][ordem+1]))

res = maior*dd
print("\nErro: %.7f * %.7f = %.7f"%(maior, dd, res))

print()
ent = float(input("Resolver para y = "))
soma = 0
print()
for i in range(n):
    px = matriz[i][i]

    for j in range(i):
        px *= (ent - y[j])
    
    soma += px
print("Resultado: %.7f"%soma);