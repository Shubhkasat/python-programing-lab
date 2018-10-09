def armstrong(x):
 sum=0
 t=x
 while(t>0):
          d=t%10
          sum+=d**3
          t=t//10
 if sum==x:
          return "armstrong"
 else:
          return "not armstrong"


x=int(input("enter the number"))
print(armstrong(x))
