import numpy as np
from math import e

def f(x):
    f = 3*(pow(x,3)) + 6 * pow(e,x)
    return f

print("Método da Posição Falsa")
a = float(input("Escreva o valor inicial do intervalo: "))
b = float(input("Escreva o valor final do intervalo: "))
erro = float(input("Escreva o erro: ")) #tolerância
print("\n")

x = (a*f(b)-b*f(a))/(f(b)-f(a))

k = 0

while abs(f(x)) > erro:
    x = (a*f(b)-b*f(a))/(f(b)-f(a))
    print("Iteração: ",k)
    print("Intervalo inicial: {:.4f}".format(a))
    print("Intervalo final: {:.4f}".format(b))
    print("Valor do x nessa iteração: {:.4f}".format(x))
    print("Valor de f(a): {:.4f}".format(f(a)))
    print("Valor de f(b): {:.4f}".format(f(b)))
    print("Valor de f(x): {:.4f}" .format(f(x)))
    print ("b - a: {:.4f}" .format(((b - a))))
    print("\n")
   
    if f(a)*f(x)<0:
        a = a
        b = x
    elif f(x)*f(b)<0:
        a = x
        b = b
    k += 1

print("Analisar quem foi menor que a precisão: b - a ou |f(x)|")
print("A raiz vale aproximadamente: {:.4f}".format(x))