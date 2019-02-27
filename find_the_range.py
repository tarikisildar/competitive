NQ = list(map(int,input().split()))
lis1= []
lis = []
d = 0
for a in range(NQ[0]):
    c = tuple(map(int,input().split())) #rangeleri listenin içinde tuple şeklinde tutuyoruz
    lis.append(c)
    

for a in range(NQ[1]):
    b = int(input())
    f=0
    l=NQ[0]-1
    
    check = False 
    while f < l: #sayının verilen range sınırları arasında en yakın olduğu sınırı bulmak için binary search kullanıyoruz.
        mid = (f + l + 1) // 2
        if b < lis[mid][0]:
            l = mid -1
        elif b > lis[mid][1]:
            f = mid +1
        if b >= lis[mid][0] and b <= lis[mid][1]: #Aramanın sonuna gelindiğinde verilen sayı middeki tuple ın sınırları içindeyse Yes bastırıyoruz.
            print("Yes")
            check = True
            break
    if not check:
        if f<len(lis) and l >= 0 and b >= lis[f][0] and b <= lis[f][1]:
            print("Yes")
        else:
            print("No")
			
#https://www.hackerrank.com/contests/inzva-02-algorithm-1-onsite-2018/challenges/find-the-range/problem
