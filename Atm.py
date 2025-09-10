amount=int(input())
if amount%100!=0:
        print("Invalid amount,try again")
else:
        if amount>=500:
            f=amount//500
            amount=amount%500
            print("500-",f)
        if amount>=200:
            g=amount//200
            amount=amount%200
            print("200-",g)
        if amount>=100:
            h=amount//100
            print("100-",h)
