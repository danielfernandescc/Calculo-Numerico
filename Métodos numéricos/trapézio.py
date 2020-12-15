import numpy as np
import math

def f(x):
  y = np.exp(x)
  return y

def trapezio(x):
  h = x[1] - x[0]
  b = (f(x[0]) + f(x[1]))/2
  y = b*h 
  return y

def trapezioR(x):
  n = len(x)
  soma = f(x[0]) + f(x[n-1])
  for e in x[1:n-1]:
    soma = soma + 2*f(e) 
  
  h = (x[1]-x[0])/2
  y = soma*h
  return y

print("============================================")
print("REGRA DO TRAPÉZIO")
print("============================================")
print()
x = [0, 1]
print("O valor da Integral é aproximadamente: {:.4f}".format(trapezio(x)))
print("O valor do erro é aproximadamente: {:.4f}".format((1/12)*np.exp(1)))
print()

print("============================================")
print("REGRA DO TRAPÉZIO REPETIDA")
print("============================================")
print()
x = np.arange(0,1.1,0.1)
print("O valor da Integral é aproximadamente: {:.4f}".format(trapezioR(x)))
print("O valor do erro é aproximadamente: {:.4f}".format(0.01/12*np.exp(1)))
print()

print("============================================")
print("CÁLCULO DA QUANTIDADE DE SUBINTERVALOS")
print("============================================")
print()
prec = float(input('Entre com a precisão: '))
maximo = max(f(x))
h = (12*prec/maximo)**(0.5)
m = 1/h
print("Número de subintervalos: ",math.ceil(m))