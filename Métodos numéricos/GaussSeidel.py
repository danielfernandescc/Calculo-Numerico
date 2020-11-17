# Gauss Seidel Iteration

# Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (14-2*y-2*z)/24
f2 = lambda x,y,z: (11-2*x-2*z)/18
f3 = lambda x,y,z: (12-2*x-2*y)/20

# Initial setup
x0 = 1
y0 = 1
z0 = 1
count = 0

print("MÉTODO DE GAUSS-SEIDEL")
print()
# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Gauss Seidel Iteration

print('Passo', count)
print('x = %0.3f\ny = %0.3f\nz = %0.3f\n' %(x0,y0,z0))
count+=1;

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('Passo ', count)
    print('x = %0.3f\ny = %0.3f\nz = %0.3f\n' %(x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    prec = max(e1, e2, e3)
    prec2 = prec/max(x1,y1,z1)

    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = prec>e or prec2>e
    
    if(prec>e):
        print('Precisão d%d = %0.3f > %.3f'%(count,prec, e))
    else:
        print('Precisão d%d = %0.3f < %.3f'%(count,prec, e))
    
    if(prec2>e):
        print('Precisão dr = %0.3f > %.3f\n'%(prec2,e))
    else:
        print('Precisão dr = %0.3f < %.3f\n'%(prec2,e))
    
    count += 1

print('Solução: x = %0.3f, y = %0.3f and z = %0.3f\n'% (x1,y1,z1))