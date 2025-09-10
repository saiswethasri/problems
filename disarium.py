n=int(input())
n1=n2=n
count=0
while n1>0:
        count=count+1
        n1=n1//10
sum=0
while n2>0:
        digit=n2%10
        sum=sum+(digit**count)
        count=count-1
        n2=n2//10
if sum==n:
        print(n,"is a disarium number")
else:
        print(n,"is not a disarium number")