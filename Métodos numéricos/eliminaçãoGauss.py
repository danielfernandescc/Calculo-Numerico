import numpy as np

a = np.array([[2.0,-1.0,0.0,1.0], #linha 0
             [-1.0,2.0,-1.0,0.0], #linha 1
             [0.0,-1.0,2.0,0.0]]) #linha 2

b = np.array([1,0,0])

n = np.size(b) #tamanho da matriz b

print("Eliminação das linhas:")
for k in range(n-1):
    for i in range(k+1,n):
        m = a[i,k]/a[k,k] #pivô(k,k) multiplicador
        a[i,:] = a[i,:] - m* a[k,:] #linha 1 recebe linha 1 - multiplicador x a linha 0
        b[i] = b[i]- m* b[i]
        print(a)
        print(" ")


def MetodoGauss(m):
    #eliminação de colunas
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    #Resolver por substituição
    ans = []
    m.reverse() 
    for sol in range(len(m)):
            if sol == 0:
                ans.append(m[sol][-1] / m[sol][-2])
            else:
                inner = 0
                #Substituir em todos os coeficientes conhecidos
                for x in range(sol):
                    inner += (ans[x]*m[sol][-2-x])
                #A equação está agora reduzida a ax + b = c
                #Resolve-se com (c - b) / a
                ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans

print("Solução do sistema: ")  
print(MetodoGauss([[2.0,-1.0,0.0,1.0],
               [-1.0,2.0,-1.0,0.0],
               [0.0,-1.0,2.0,0.0,]]))