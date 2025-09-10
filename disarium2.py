n=int(input())
count=1
sum=0
while n>0:
        digit=n%10
        sum=sum+(digit**count)
        count=count+1
        n=n//10
print(sum)