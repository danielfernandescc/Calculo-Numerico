MAX = 100;
 
def luDecomposition(mat, n):
 
    lower = [[0 for x in range(n)] 
                for y in range(n)];
    upper = [[0 for x in range(n)] 
                for y in range(n)];
    
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
            print("Passo", i, "- Matriz L")
            for c in range(3):
                for s in range(3):
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
# Driver code
mat = [[3, 2, 4],
       [1, 1, 2],
       [4, 3, 2]];

b = [1, 2, 3]

luDecomposition(mat, 3);