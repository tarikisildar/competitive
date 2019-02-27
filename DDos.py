n = int(input())
arr = list(map(int, input().split()))
mx = 0
for i in range(n):
    c = 0
    co = 0
    for e in range(i,n):
        c+= arr[e] #listenin içinde her eleman için kalan elemanları sırayla ekliyoruz
        if c / (e-i+1) > 100 and e-i+1 > mx: # şimdiye kadarki toplamın a. ortalaması 100den büyükse ve eleman sayısı önceki maksimumdan büyükse yeni maksimumu belirliyoruz.
            mx = e-i+1
print(mx)

#https://codeforces.com/contest/1057/problem/B
