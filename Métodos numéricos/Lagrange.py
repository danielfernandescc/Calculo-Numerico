# Lagrange Interpolation

# Importing NumPy Library
import numpy as np

# Reading number of unknowns
print("FORMA DE LAGRANGE")
print()
print("---------------------------------------")
n = int(input('Digite a quantidade de nós: '))
print("---------------------------------------")
print()

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))

# Reading data points
print('Entre com os valores de x e f(x), sabendo que y = f(x): ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']= '))
    y[i] = float(input( 'y['+str(i)+']= '))

fim = ""
print()

# Implementing Lagrange Interpolation
for i in range(n):
    num = ""
    den = 1
    res = ""
    
    for j in range(n):
        if i != j:
            if(x[j] > 0):
                num += "(x - " + str(abs(x[j])) + ")"
                den *= (x[i] - x[j])
            elif(x[j] < 0):
                num += "(x + " + str(abs(x[j])) + ")"
                den *= (x[i] - x[j])
            else:
                num += "x"
                den *= x[i]
    denom = '%.3f'%den

    res += num + "/" + denom
    if(i!=n-1):
        fim += str(y[i]) + res + " + "
    else:
        fim += str(y[i]) + res
    print("L"+str(i)+"(x) =",res)
    print()

# Displaying output
print("P%d(x) ="%i, fim)
print()

ent = float(input("Resolver para x = "))

res = 0
for i in range(n):
    num = 1
    den = 1
    
    for j in range(n):
        if i != j:
            num *= (ent - x[j])
            den *= (x[i] - x[j])

    res += y[i]*(num/den)
    
print("P%d(%.2f) = %.3f"%(i,ent,res))
print()