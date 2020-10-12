import math
from math import e

print("Método da Bissecção")
print("\n")

def funcao (x):
   return pow(x,2) + math.log(x) #função a ser calculada a raiz
a = float(input("Intervalo a: ")) #inicio do intervalo
b = float(input("Intervalo b: ")) #fim do intervalo
precisao = float(input("Precisão: ")) #limite do E
print ('\n')

if (b - a ) < precisao:
   raiz = a
else:
   k = 1
   f = funcao(a)
   while True:
      x = (a + b)/2
      print ("Iteracao: %d" % (k))
      print("Intervalo inicial: {:.4f}".format(a))
      print("Intervalo final: {:.4f}".format(b))
      print ("Valor de X: %f" % (x))
      print ("f(x): %f" % (funcao(x)))
      print ("b - a: %f" % ((b - a)))
      print ('\n')

      if f * funcao(x) > 0:
         a = x
      else:
         b = x
      if (b - a) <= precisao:
         raiz = (a + b)/2
         print ("Iteracao: %d" % (k+1))
         print("Intervalo inicial: {:.4f}".format(a))
         print("Intervalo final: {:.4f}".format(b))
         print ("Valor de X: %f" % ((a + b)/2))
         print ("f(x): %f" % (funcao((a + b)/2)))
         print ("Valor de b - a: {:.4f}, cujo valor é menor que a precisão" .format(((b - a))))
         print("PARAR")
         print("\n")
         break
      k = k + 1

print ('Valor aproximado da raiz : %f' % (raiz))