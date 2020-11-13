# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknowns
print("A matriz começa com [0][0], ou seja, vai de 0 até a quantidade de elementos da linha -1")
print("Digitar linha por linha")
print()
print("------------------------------------------------------")
n = int(input('Número do tamanho da matriz: '))
print("------------------------------------------------------")
print()


# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients

print('Coeficientes da matriz aumentada:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divisão por zero detectada!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
    
    print()
    print("Eliminação de Gauss: ", i+1)
    print()
    print(a)

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

print("\n")
print("Matriz Escalonada: \n")
print(a)

# Displaying solution
print('\nSolução do sistema: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')