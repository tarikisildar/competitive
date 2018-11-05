import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    lis = [] #list for holding ratings, indexes and candie counts
    sm = 0
    for i in range(len(arr)):
        lis.append([arr[i],i,0])
    lis.sort() #sort the list by ratings
    visited = {}
    for i in range(len(arr)):
        if lis[i][0] == arr[lis[i][1]-1]: # if this one's rating equals to one before
            if lis[i][1]+1 in visited.keys(): # if we gave candy to next one we'll give this one 1 more than next one because rating of that is bigger.
                lis[i][2] = visited[lis[i][1]+1] + 1
                visited[lis[i][1]] = lis[i][2]
            else: # if there are no candy in next, we give this a candy.
                lis[i][2] = 1
                visited[lis[i][1]] = 1
        elif lis[i][1]+1 in visited.keys() or lis[i][1]-1 in visited.keys(): #if we gave candy next ones.
            try:
                lis[i][2] = max(visited[lis[i][1]+1],visited[lis[i][1]-1]) + 1
            except:
                try:
                    lis[i][2] = visited[lis[i][1]+1] + 1
                except:
                    lis[i][2] = visited[lis[i][1]-1] + 1
            visited[lis[i][1]] = lis[i][2]
        else:
            lis[i][2] = 1
            visited[lis[i][1]] = 1
    print(lis)
    for i in lis: #sum of all candies
        sm += i[2]
    return sm
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
# https://www.hackerrank.com/challenges/candies/copy-from/89811348
