#importa o modulo math  
import math 
#from math import e

#cria a funcao(x)
def funcao (x):
   return ((pow(x,5)) - 5 * math.pow(x,2) + 1)


#cria a derivada da funcao(x)
def funcaoLinha(x):
   return (5 * math.pow(x,4) - 10 * x)

print("Método de Newton Raphson")
print("\n")
#Leitura dos dados
#Le o valor inicial de x      
x = float(input("Digite o valor de x0: "))
#Le precisao 1
precisao1 = float(input("Precisao1: "))
#Le precisao 2
precisao2 = float(input("Precisao2: "))
print ('\n')

if (math.fabs(funcao(x))) < precisao1:
   xBarra = x   
else:
   k = 1
   flag = True
   while flag:
      x1 = x - (funcao(x) / funcaoLinha(x))
      print ("Iteracao: %d" % (k))
      print ("Valor de X: {:.4f}".format((x1)))
      print ("f(x): {:.4f}".format((funcao(x1))))
      print("x1 - x: {:.4f}".format(x1-x))
      print ('\n')

      if (math.fabs(funcao(x1))) < precisao1 or (math.fabs(x1 - x)) < precisao2:
         xBarra = x1
         flag = False
      x = x1
      k = k + 1

#Resultado final. Valor de xBarra    
print("Verificar qual dos dois quesitos de parada satisfazem a resposta: x1 - x ou |f(x1)|")  
print ('Valor aproximado da raiz: %f' % (xBarra))