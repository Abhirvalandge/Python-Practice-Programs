# Find the fctorial of given number

no=int(input("Enter No:"))
result=1
for x in range(no,0,-1):
    result*=x
print(result)