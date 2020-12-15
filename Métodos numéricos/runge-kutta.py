import math
def F(x, y):
  return 9/(2*y)

def heun(x0, y0, h, end, e):
  x = x0
  y = y0
  while abs(x-end) >= e:
    y = y + h/2*(F(x, y) + F(x+h, y + h*F(x, y)))
    x += h
    print("Valor do subintervalo: {:.3f} \t\t\t Valor de y nesse subintervalo: {:.3f}" .format(x, y))
  print()
  return y

print("================================================================")
print("MÉTODO DE RUNGE-KUTTA DE SEGUNDA ORDEM PARA EDO")
print("================================================================")
print()

x0 = float(input("Insira o valor de x0:  "))
y0 = float(input("Insira o valor de y0:  "))
h = float(input("Insira o valor do passo h: "))
end = float(input("Insira o valor de x que se deseja a aproximação: "))
print()

print("A aproximação final é: {:.3f}".format(heun(x0, y0, h, end, 0.000001)))