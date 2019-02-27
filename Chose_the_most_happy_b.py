a = int(input())
arr = list(map(int,input().split()))
sarr = []
for i in range(len(arr)):
    sarr.append(arr[i] - (i+1)) #B değeri eklenmeden kalan sonuçlardan oluşan bi liste oluşturuyoruz
    
sarr.sort()
b = sarr[int(a/2)] #listenin medyan değeri kullanılması gereken b yi veriyor
b1 = sarr[int(a/2)+1]# liste uzunluğunun çift sayı olması durumu için 2 değere bakıyoruz.
c = 0
c1 = 0

for i in range(a):
    c += abs(arr[i] - (b+i+1)) 
    c1 += abs(arr[i] - (b1+i+1)) 
print(min(c,c1))

#https://www.hackerrank.com/contests/inzva-02-algorithm-1-online-2018/challenges/choose-the-most-happy-b/proble
