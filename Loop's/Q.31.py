# Input any 4 digit number and find out the sum of first and last digit

no=int(input("Enter No:"))
fno=no%10
while no!=0:
    rem=no%10
    no=no//10

print("Sum :",fno+rem)