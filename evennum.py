n=int(input())
sum=0
while n!=0:      
    digit=n%10
    if digit%2==0:
            sum=sum+digit
    n=n//10
print(sum)
