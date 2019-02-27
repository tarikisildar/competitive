nl = list(map(int,input().split()))
arr = list(map(int,input().split()))

arr.sort()

mx=0 
for i in range(len(arr)-1):
    if arr[i+1] - arr[i] > mx:
        mx = arr[i+1] - arr[i]
mx/=2
if arr[0] > mx:
    mx = arr[0]
if nl[1] - arr[-1] > mx:
    mx = nl[1] - arr[-1]
print(mx)

#https://www.hackerrank.com/contests/inzva-02-algorithm-1-online-2018/challenges/fasho-and-street/problem
