# Input any 4 digit number and reverse it

no=int(input("Enter no:"))
rev = 0
while no!=0:
    rem = no%10
    no = no // 10
    rev = (rev*10)+rem
print ("Reverse No: ",rev)