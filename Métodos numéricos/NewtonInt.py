import numpy as np

# Reading number of unknowns
print("FORMA DE NEWTON")
print()
print("-----------------------------------------")
n = int(input('Digite a quantidade de nós: '))
print("-----------------------------------------")
print()

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))
matriz = [[" " for i in range(n)] for j in range(n)]

# Reading data points
print('Digite os valores de x e f(x), sabendo que y = f(x): ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']= '))
    y[i] = float(input( 'y['+str(i)+']= '))
    matriz[i][0] = y[i]

print()
for i in range(1, n):
    k = 0
    for j in range(i, n):
        matriz[j][i] = (matriz[j][i-1] - matriz[j-1][i-1])/(x[j] - x[k])
        k += 1
        
for i in range(n):
    print("Ordem", i, end='\t')
print()

for i in range(n):
    for j in range(n):
        if(matriz[i][j] != " "): print("%.3f"%matriz[i][j], end="\t")
        else:                    print(" ", end="\t")
    print()

print()
for i in range(n):
    if(matriz[i][i]>=0): print(" + %.3f"%matriz[i][i], end= "")
    else:                print(" - %.3f"%abs(matriz[i][i]), end= "")

    for j in range(i):
        if(x[j]>=0):  print("(x-%.3f)"%x[j], end= "")
        elif(x[j]<0): print("(x+%.3f)"%abs(x[j]), end= "")

print("\n")
for i in range(n):
    if(matriz[i][i]>0):
        print(" + %.3f"%matriz[i][i], end= "")
        for j in range(i):
            if(x[j]>0):   print("(x-%.3f)"%x[j], end= "")
            elif(x[j]<0): print("(x+%.3f)"%abs(x[j]), end= "")
            else:         print("(x)", end= "")
    elif(matriz[i][i]<0):
        print(" - %.3f"%abs(matriz[i][i]), end= "")
        for j in range(i):
            if(x[j]>0):   print("(x-%.3f)"%x[j], end= "")
            elif(x[j]<0): print("(x+%.3f)"%abs(x[j]), end= "")
            else:         print("(x)", end= "")

print("\n")

ent = float(input("Resolver para x = "))
soma = 0
print()
for i in range(n):
    px = matriz[i][i]

    for j in range(i):
        px *= (ent - x[j])
    
    soma += px
print("Resultado: %.3f"%soma);
print()

erro = float(input("Calculo do Erro: "))
ordem = int(input("Ordem: "))
ap = int(input("A partir de qual linha? "))

maior = 1.0
for i in range(ap, ap+3):
    maior *= (erro-x[i])

maior = abs(maior)

dd = 0
for i in range(ordem+1, n):
    if(abs(matriz[i][ordem+1]) > dd): dd = float(abs(matriz[i][ordem+1]))

res = maior*dd
print("\nErro: %.3f * %.3f = %.3f\n"%(maior, dd, res))