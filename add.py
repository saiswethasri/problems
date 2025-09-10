import math
n=int(input("Enter the n value:"))
last=n%10
first=n//10**int(math.log10(n))
print(last + first)