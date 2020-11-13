# Python3 program to decompose
# a matrix using Cholesky
# Decomposition 
import math 
MAX = 100; 

def Cholesky_Decomposition(matrix, n): 
    count = 0
    lower = [[0 for x in range(n + 1)]
                for y in range(n + 1)]; 

    # Decomposing a matrix 
    # into Lower Triangular 
    for i in range(n):
        for j in range(i + 1):
            count+=1
            sum1 = 0; 

            # sum1mation for diagnols 
            if (j == i):
                for k in range(j): 
                    sum1 += pow(lower[j][k], 2); 
                lower[j][j] = float(math.sqrt(matrix[j][j] - sum1));
                
            else: 

                # Evaluating L(i, j) 
                # using L(j, j) 
                for k in range(j): 
                    sum1 += (lower[i][k] *lower[j][k]); 
                if(lower[j][j] > 0): 
                    lower[i][j] = float((matrix[i][j] - sum1) / 
                                               lower[j][j]);
                
            print("Passo", count, "- Matriz G")
            for c in range(3):
                for s in range(3):
                    #print(lower[c][s], end="\t\t\t")
                    print("{:.3f}".format(lower[c][s]), end = "\t")
                print()
            print()

    # Displaying Lower Triangular 
    # and its Transpose 
    print("Triangular Inferior - G\t\tTransposta - Gt"); 
    for i in range(n):

        # Lower Triangular 
        for j in range(n): 
            print("{:.3f}".format(lower[i][j]), end = "\t")
        print("", end = "\t"); 

        # Transpose of 
        # Lower Triangular 
        for j in range(n): 
            print("{:.3f}".format(lower[j][i]), end = "\t")
        print(""); 

# Driver Code 
n = 3; 
matrix = [[4, -2, 4],
          [-2, 2, -1],
          [4, -1, 9]];

b = [2, 1, 8]

Cholesky_Decomposition(matrix, n); 