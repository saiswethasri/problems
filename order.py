print("***Canteen Menu***")
print("1.water bottle - 20")
print("2.fried rice-80")
print("3.noodles-90")
option=int(input("Enter your option:"))
if option==1:
    n=int(input("Enter no.of bottles"))
    bill=n*20
elif option==2:
    n=int(input("Enter the no.of fired rices:"))
    bill=n*80
elif option==3:
    n=int(input("Enter the no.of noodles:"))
    bill=n*90
else:
    print("Invalid option,try again")
print("Your bill is:",bill)