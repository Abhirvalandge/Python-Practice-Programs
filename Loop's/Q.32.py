# Input any 4 digit number and find out the sum of middle digits.

no=int(input("Enter No:"))
while no!=10:
    rem1 = no % 10
    no = no // 10
    rem2 = no % 10
    no = no // 10
    rem3 = no % 10
    no = no // 10
    rem4 = no % 10
    no = no // 10
    break

print("sum of middle no:",rem2+rem3)