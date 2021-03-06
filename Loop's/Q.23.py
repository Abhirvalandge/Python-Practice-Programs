# WAP to check the number is prime or not

no=int(input("Enter No:"))
b=0
for i in range(1,no+1):
    if no%i==0:
        b+=1
if b==2:
    print(no,"is a prime")
else:
    print(no,"is not a prime")