import collections

lis = []
n = int(input())
dic = collections.defaultdict(list)
for i in range(n):
    lis.append(tuple(map(int,input().split())))

lis.sort(reverse=True)

for i in range(n):
    dic[lis[i][1]-lis[i][0]].append(lis[i])
lis1 = list(map(int,input().split()))
st = ""
mx1= (-1,-1)
mx2 = (-1,-1)
for i in lis1:
    if dic[i]:
        a = dic[i].pop()
        if (a>= mx1) or a >=mx2:
            
            if mx1[0] < a[0]:
                mx1 = a
            if mx2[1] < a[1]:
                mx2 = a
            
            st+=str(a[0]) + " " + str(a[1])+"\n"
        else:
            print("NO")
            exit()
    else:
        print("NO")
        exit()
print("YES")
print(st,end="")
#https://codeforces.com/problemset/problem/596/C
