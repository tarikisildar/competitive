n,x,y = map(int,input().split())
from collections import defaultdict
import sys
sys.setrecursionlimit(1500)
count = 0
class Graph: 
    sub= 0
    chk = 0
    
    def __init__(self,x,y): 
        self.x = x
        self.y = y
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def DFSUtil(self,v,visited): 
        global count
        visited[v]= True
        if (v == self.x):
            self.chk[v] = True
        
        #print(visited)
        for i in self.graph[v]:
            
            if visited[i] == False:
                self.sub[v] += self.DFSUtil(i, visited)
                self.chk[v] |= self.chk[i]
  
        return self.sub[v]
    def DFS(self,v): 

        visited = [False]*(len(self.graph))
        self.sub = [1]*(len(self.graph))
        self.chk = [False]*(len(self.graph))
        
        self.DFSUtil(v,visited)
g = Graph(x-1,y-1)
for i in range(n-1):
    a,b = map(int,input().split())
    g.addEdge(a-1,b-1)
    g.addEdge(b-1,a-1)
g.DFS(y-1)
fin = 0
for i in g.graph[y-1]:
    
    if g.chk[i]:
        fin = g.sub[y-1] - g.sub[i]
        break

print(n*(n-1)-fin*g.sub[x-1])
