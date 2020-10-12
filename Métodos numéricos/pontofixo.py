import math

print("Método do ponto fixo")
print("\n")

def f(x): #função para o exercício
    return pow(x,3) - 9 * x + 3 #pode escolher qualquer função

def g(x): #função de iteração
    return ((pow(x,3)/9) + 1 / 3)

def pontoFixo():
    x0 = float(input("Digite a aproximação inicial: "))
    iteracoes = int(input("Dgite a quantidade de iterações: ")) #pode-se atribuir uma tolerância de erro também.
    #erro = float(input("Digite a precisão: "))
    print("\n")
    iteracao = 0
    x1 = 0
    while iteracao < iteracoes:
        x1 = g(x0)
        x0 = x1
        print("Iteração: ",iteracao)
        print("f(x): {:.4f}" .format(f(x1)))
        print("g(x): {:.4f}" .format(g(x1)))
        print("x: {:.4f}" .format(x1))
        print("\n")
        iteracao += 1
    
    #SE HOUVER ERRO USAR: print("x1 - x0: {:.4f}".format(x1-x0))
    print("Analisar os critérios de parada: x1 - x0 ou |f(x0)| se um é menor que a precisão")
    print("Caso não formos usar precisão, quando as casas repetirem nós encontramos a raiz")
    print("A raiz vale aproximadamente: {:.4f}".format(x1))
pontoFixo()