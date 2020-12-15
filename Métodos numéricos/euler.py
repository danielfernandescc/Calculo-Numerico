import math

def F(x, y):
  return 2 * x + 3

print("=========================================")
print("MÉTODO DE EULER PARA EDO")
print("=========================================")
x0 = float(input("Insira o valor de x0: "))
y0 = float(input("Insira o valor de y0: "))
h = float(input("Insira o valor do passo h: "))
n = float(input("Insira o valor de x que se deseja a aproximação: "))
print()

while True:
  print("Valor do subintervalo: {:.3f} \t\t\t Valor de y nesse subintervalo: {:.3f}" .format(x0, y0))
  if(abs(x0 - n) < 0.000001):
    break
  y0 = y0 + F(x0, y0)*h
  x0 += h

print()
print("A aproximação final é: {:.3f}".format(y0))