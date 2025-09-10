total_bill=0
bill=0
ch=input("Do you want to order something:")
while ch=='Y' or ch=='y':
        print("***Canteen Menu***")
        print("1.water bottle - 20")
        print("2.fried rice-80")
        print("3.noodles-90")
        option=int(input("Enter your option:"))
        if option==1:
                n=int(input("Enter no.of bottles"))
                bill=n*20
        elif option==2:
                n=int(input("Enter the no.of fried rices:"))
                bill=n*80
        elif option==3:
                n=int(input("Enter the no.of noodles:"))
                bill=n*90
        else:
                print("Invalid option,try again")
        total_bill=total_bill+bill
        ch=input("Do you want to order something:")
print("Your total bill is:",total_bill)
