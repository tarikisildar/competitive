import math
st = input()
def pal(st,mark):
   bo = st == st[::-1]
   nst = ""
   
   if len(st)==1:
      return mark
   if bo and len(st)%2 ==1:
      nst = st[len(st)//2+1:]
      mark = False
   elif bo:
      nst = st[len(st)//2:]
   
   if nst == nst[::-1]:
      return pal(nst,mark)
   else:
      return mark

boo = pal(st,True)
if (st[:len(st)//2] == st[0]*(len(st)//2) and st[math.ceil(len(st)/2):]==st[0]*(len(st)//2)):
   print("Impossible")
elif len(st)%2 == 0 and boo:
   print(1)
else:
   print(2)
#https://codeforces.com/contest/1109/problem/B
