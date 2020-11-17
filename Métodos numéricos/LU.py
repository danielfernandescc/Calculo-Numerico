MAX = 100;
 
def luDecomposition(mat, b, n):
 
    lower = [[0 for x in range(n)] 
                for y in range(n)];
    upper = [[0 for x in range(n)] 
                for y in range(n)];
    
    print("FATORAÇÃO LU")
    print()
    
    for i in range(n):
        lower[i][i] = 1

    # Decomposing matrix into Upper 
    # and Lower triangular matrix
    for i in range(n):
 
        # Upper Triangular
        for k in range(i, n):
 
            # Summation of L(i, j) * U(j, k)
            sum = 0;
            for j in range(i):
                sum += (lower[i][j] * upper[j][k]);
 
            # Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum;

        if(i!=0):
            print("Passo", i, "- Matriz M: ", i - 1)
            for c in range(n):
                for s in range(n):
                    print("{:.3f}".format(lower[c][s]), end = "\t")
                print()
            print()
        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1; # Diagonal as 1
            else:
 
                # Summation of L(k, j) * U(j, i)
                sum = 0;
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i]);
 
                # Evaluating L(k, i)
                lower[k][i] = float((mat[k][i] - sum) /
                                       upper[i][i]);
        print()
 
    # setw is for displaying nicely
    print("Tringular Inferior - L \t\t\t Triangular Superior - U");
    # Displaying the result :
    for i in range(n):
        # Lower
        for j in range(n):
            print("{:.3f}".format(lower[i][j]), end = "\t")
        print("", end = "\t\t");

        for j in range(n):
            print("{:.3f}".format(upper[i][j]), end = "\t")
        print("", end = "");
        print()

    y = [0 for i in range(n)]
    y[0] = b[0]/lower[0][0]
    #y[1] = (-y[0]*lower[1][0]+b[1])/lower[1][1]
    #y[2] = (-y[0]*lower[2][0]-y[1]*lower[2][1]+b[2])/lower[2][2]
    #y[3] = (-y[0]*lower[3][0]-y[1]*lower[3][1]-y[2]*lower[3][2]+b[3])/lower[3][3]
    y[0] = round(y[0], 5)
    print("\nValores matriz Ly = b")
    print("y1 = %.3f"%y[0])
    for j in range(1, n):
        num = 0
        for k in range(0,j):
            num-=lower[j][k]*y[k]
        num+=b[j]
        num = round(num, 5)
        y[j] = num/lower[j][j]
        
        print("y%d = %.3f"%(j+1, y[j]))
    
    x = [0 for i in range(n)]
    x[n-1] = y[n-1]/upper[n-1][n-1]
    #x[n-2] = (-x[n-1]*upper[n-2][n-1]+y[n-2])/upper[n-2][n-2]
    #x[n-3] = (-x[n-1]*upper[n-3][n-1]-x[n-2]*upper[n-3][n-2]+y[n-3])/upper[n-3][n-3]
    #x[n-4] = (-x[n-1]*upper[n-4][n-1]-x[n-2]*upper[n-4][n-2]-x[n-3]*upper[n-4][n-3]+y[n-4])/upper[n-4][n-4]

    for i in range(n-2, -1, -1):
        num = 0
        for j in range(n-1, i, -1):
            num-=x[j]*upper[i][j]
        num+=y[i]
        num = round(num, 5)
        x[i] = num/upper[i][i]
    
    print("\nValores matriz Ux = y")
    for i in range(n):
        print("x%d = %.3f"%(i+1, x[i]))
 
# Driver code
mat = [[1, 9, 9],
       [9, 150, 7],
       [9, 7, 1000]];

b = [2, -1, 3]

luDecomposition(mat, b, 3);