n=int(input())
sum1=sum2=0
place1=place2=1
while n>0:      
    digit=n%10
    if digit%2==0: 
            sum1=digit*place1+sum1
            place1*=10
    else:
            sum2=digit*place2+sum2
            place2*=10
    n=n//10
print(sum1-sum2)