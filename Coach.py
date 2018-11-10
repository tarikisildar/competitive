import sys
nm = list(map(int, input().split()))
done = []
visited = []
for i in range(nm[1]):
    pair = input().split()
    if pair[0] not in visited and pair[1] not in visited:
        done.append([pair[0],pair[1]])
        visited.append(pair[0])
        visited.append("-")
        visited.append(pair[1])
    elif pair[0] not in visited:
        temp = visited.index(pair[1])
        if temp < len(visited)-1 and visited[temp+1] != "-":
            if temp < len(visited)-1 and visited[temp+1] == "|":
                print("-1")
                sys.exit()
            visited.insert(temp+1,"-")
            visited.insert(temp+2,pair[0])
            #visited.insert(temp+3,"|")
            
        else:
            if temp < len(visited)-3 and visited[temp+3] == "|":
                print("-1")
                sys.exit()
            visited.insert(temp+4,"-")
            visited.insert(temp+5,pair[0])
            #visited.insert(temp+6,"|")
            
    elif pair[1] not in visited:
        temp = visited.index(pair[0])
        if temp <len(visited)-1 and visited[temp+1] != "-":
            if temp < len(visited)-1 and visited[temp+1] == "|":
                print("-1")
                sys.exit()
            visited.insert(temp+1,"-")
            visited.insert(temp+2,pair[1])
            #visited.insert(temp+3,"|")
            
            
        else:
            if temp < len(visited)-3 and visited[temp+3] == "|":
                print("-1")
                sys.exit()
            visited.insert(temp+4,"-")
            visited.insert(temp+5,pair[1])
            #visited.insert(temp+6,"|")    

k = 0

lis = [[] for i in range((int(nm[0])//3)*2)]
i = 0
while i<len(visited)-1:
    if visited[i+1] == "-":
        lis[k].append(visited[i])
        i+=2
    else:
        lis[k].append(visited[i])
        k+=1
        i+=1

i = 0
while i < len(lis):
    if lis[i] == []:
        lis.pop()
        i-=1
    i+=1

if len(visited) > 2:
    lis[-1].append(visited[-1])

for i in range(nm[0]):
    flag = False

    if str(i+1) not in visited:
        for e in range(len(lis)):
            if len(lis[e]) < 3:
                lis[e].append(str(i+1))
                    
                flag = True
                break
        if not flag:
            lis.append([str(i+1)])

for i in lis:
    if len(i) != 3:
        print(-1)
        sys.exit()
for i in lis:
    print(i[0],i[1],i[2])
#http://codeforces.com/problemset/problem/300/b
