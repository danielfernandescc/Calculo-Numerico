import math
from math import e

def f(x):
    return (math.sqrt(x)- (5 * pow(e,-x)))

print("Método da secante")
print("\n")

xn = 0.0
x = []
n0 = 100 # quantidade máxima de iterações (opcional)

a = float(input("Escreva o valor inicial do intervalo: "))
b = float(input("Escreva o valor final do intervalo: "))
erro = float(input("Escreva o primeiro erro: ")) #tolerância
#erro2 = float(input("Escreva o segundo erro: "))
print("\n")

x.append(a)
x.append(b)

i = 0
n = 1

while(math.fabs(f(xn)) > erro):
    xn = x[n] - (x[n]-x[n-1]) / (f(x[n]) - f(x[n-1]))*f(x[n])
    x.append(xn)
    n = n + 1
    i = i + 1

    print ("Iteracao: %d" % (i))
    print ("Valor de X: {:.4f}".format((xn)))
    print ("f(x): {:.4f}".format((f(xn))))
    print ('\n')

    if(i >= n0):
        break

print("Verificar se algum dos critérios de parada foi alcançado: x1 - x0 ou |f(x1)| se um for menor que a precisão")
print("\nRaiz: %.4f\niterações: %i\nf(%.2f) = %.2f\n"%(xn,i,xn,f(xn)))