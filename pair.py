n1=int(input())
n2=int(input())
s1=s2=0
for i in range(1,n1+1):
    if n1%i==0:
        s1=s1+i
for i in range(1,n2+1):
    if n2%i==0:
        s2=s2+i
if (s1//n1) == (s2//n2):
    print("Friendly pair")
else:
    print("Not friendly pair")
