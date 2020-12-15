import math

def f(x):
  return 1/(x**2)

def integral(x0, xn, h):
  res = 0
  while abs(xn - x0) >= 0.000001:
    res += f(x0) + 4*f(x0+h) + f(x0+2*h)
    x0 += 2*h
  return res*h/3

print("======================================================")
print("REGRA 1/3 DE SIMPSON SIMPLES")
print("======================================================")
print()

x0 = float(input("Digite o valor do limite inferior: "))
xn = float(input("Digite o valor do limite superior: "))
h = float(input("Digite o tamanho do intervalo h: "))
print()

print("O valor da integral é: {:.4f}".format(integral(x0, xn, h)))