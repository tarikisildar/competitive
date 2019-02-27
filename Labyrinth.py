import collections
n,m = map(int,input().split())
r,c = map(int,input().split())
x,y = map(int,input().split())
arr = []

for i in range(n):
   arr.append(input())

que = collections.deque([(r-1,c-1)])
dist = [[float("inf")]*m for i in range(n)] #left moves needed from start to target
dist[r-1][c-1] = 0

while que: #look up down right and left if left is available append to back of queue else front
    v = que.popleft()
    if v[0]>0 and arr[v[0]-1][v[1]] != "*" and dist[v[0]-1][v[1]] > dist[v[0]][v[1]]:
        dist[v[0]-1][v[1]] = dist[v[0]][v[1]]
        que.appendleft((v[0]-1,v[1]))
    if v[0]<n-1 and arr[v[0]+1][v[1]] != "*" and dist[v[0]+1][v[1]] > dist[v[0]][v[1]]:
        dist[v[0]+1][v[1]] = dist[v[0]][v[1]]
        que.appendleft((v[0]+1,v[1]))
    if v[1]<m-1 and arr[v[0]][v[1]+1] != "*" and dist[v[0]][v[1]+1] > dist[v[0]][v[1]]:
        dist[v[0]][v[1]+1] = dist[v[0]][v[1]]
        que.appendleft((v[0],v[1]+1))
    if v[1]>0 and arr[v[0]][v[1]-1] != "*" and dist[v[0]][v[1]-1] > dist[v[0]][v[1]]+1:
        dist[v[0]][v[1]-1] = dist[v[0]][v[1]]+1 #left distance increase
        que.append((v[0],v[1]-1))
    
count = 0
for i in range(n):
    for e in range(m):
        if dist[i][e] <= x and e-(c-1)+dist[i][e] <= y:
            count+=1
print(count)
#https://codeforces.com/problemset/problem/1063/B
