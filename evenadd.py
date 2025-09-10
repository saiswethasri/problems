n=int(input())
sum=0
place=1
while n>0:      
    digit=n%10
    if digit%2==0:
            sum=digit*place+sum
            place=place*10
    n=n//10
print(sum)