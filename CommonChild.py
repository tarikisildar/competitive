
import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(X, Y, visited):
    m = len(s1)
    n = len(s2)
    for i in range(m+1):
        for e in range(n+1):
            if i == 0 or e == 0:
                visited[i][e] = 0
            elif X[i-1] == Y[e-1]:
                visited[i][e] = visited[i-1][e-1] + 1
            else:
                visited[i][e] = max(visited[i-1][e], visited[i][e-1])
    return visited[m][n]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()
    visited = [[None] * (len(s1)+1)  for e in range(len(s2)+1)] #empty matrix
    
    result = commonChild(s1, s2, visited)

    fptr.write(str(result) + '\n')

    fptr.close()
    
# https://www.hackerrank.com/challenges/common-child/problem
