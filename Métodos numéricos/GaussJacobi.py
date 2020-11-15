# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (7-2*y-z)/10
f2 = lambda x,y,z: (-8-x-z)/5
f3 = lambda x,y,z: (6-2*x-3*y)/10

# Vetor para as iterações
x0 = 0
y0 = 0
z0 = 0
count = 0

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Jacobi Iteration

print('Passo', count)
print('x = %0.2f\ny = %0.2f\nz = %0.2f\n' %(x0,y0,z0))
count+=1;

condition = True
print()
while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x0,y0,z0)
    z1 = f3(x0,y0,z0)
    print('Passo', count)
    print('x = %0.4f\ny = %0.4f\nz = %0.4f\n' %(x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    prec = max(e1, e2, e3)
    prec2 = prec/max(abs(x1),abs(y1),abs(z1))
    
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = prec>e or prec2>e

    if(prec>e):
        print('Precisão d%d = %0.4f > %.4f'%(count,prec, e))
    else:
        print('Precisão d%d = %0.4f < %.4f'%(count,prec, e))
    
    if(prec2>e):
        print('Precisão dr = %0.4f > %.4f\n'%(prec2,e))
    else:
        print('Precisão dr = %0.4f < %.4f\n'%(prec2,e))
    

    count += 1

print('Solução: x = %0.7f, y = %0.7f and z = %0.7f\n'% (x1,y1,z1))