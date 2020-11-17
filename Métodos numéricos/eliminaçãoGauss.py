# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknowns
print("ELIMINAÇÃO DE GAUSS")
print()
print("-------------------------")
n = int(input('Tamanho matriz: '))
print("-------------------------")
print()

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Coeficientes (matriz aumentada):')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']= '))

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divisão por zero!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
    print()
    if(i==n-1): print("Matriz escalonada estendida final:")
    for k in range(n):
        for l in range(n+1):
            if(l==n): print("|", end=' ')
            if(int(a[k][l])==a[k][l]): print(int(a[k][l]), end='\t')
            else: print("{:.3f}".format(a[k][l]), end='\t')
        print()

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

# Displaying solution
print('\nSolução: ')
for i in range(n):
    print('X%d = %0.3f' %(i,x[i]), end = '\t')