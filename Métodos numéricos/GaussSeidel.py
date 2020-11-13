# Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (5-y-z)/5
f2 = lambda x,y,z: (6-3*x-z)/4
f3 = lambda x,y,z: (-3*x-3*y)/6

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Digite a estimativa de erro: '))
print("\n")

# Implementation of Gauss Seidel Iteration
condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('Passo ', count)
    print('x = %0.4f\ny = %0.4f\nz = %0.4f\n' %(x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    prec = max(e1, e2, e3)
    prec2 = prec/max(x1,y1,z1)

    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = prec>e and prec2>e
    if(count!=0):
        if(condition):
            print('Precisão d%d = %0.4f > %.4f'%(count,prec, e))
            print('Precisão dr = %0.4f > %.4f\n'%(prec2,e))
        else:
            print('Precisão d%d = %0.4f < %.4f'%(count,prec, e))
            print('Precisão dr = %0.4f < %.4f\n'%(prec2,e))
    
    count += 1

print('Solução: x = %0.7f, y = %0.7f and z = %0.7f\n'% (x1,y1,z1))
print("Observe que x = x1, y = x2, z = x3")