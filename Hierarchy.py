n = int(input())
lis = list(map(int,input().split()))
m =  int(input())
edges = []
for d in range(m):
    edges.append(list(map(int,input().split())))
    
edges.sort(key  = lambda x: x[2]) #sort edges by weights
visited = []
count = 0
for i in range(m):
    if edges[i][1] not in visited: #every employee will have 1 supervisor
        visited.append(edges[i][1]) 
        count += edges[i][2]

if len(visited) == n-1:
    print(count)
else:
    print(-1)
    
# https://codeforces.com/contest/17/problem/B
