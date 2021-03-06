# Input any 4 digit number and find out the sum of the digits

no=int(input("Enter No:"))
sum=0
while no!=0:
    rem=no%10
    no=no//10
    sum=sum+rem

print("Sum :",sum)