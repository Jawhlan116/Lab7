a=int(input())
b=int(input())
c=int(input())
d=int((a+b+c)/60)
e=(a+b+c)%60
print("%.0f:"%d+str(e).zfill(2))