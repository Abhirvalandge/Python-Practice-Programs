print('List Class Methods')

print(' 1) append')
l1=[10,20,30,40,50]
print(l1)
l1.append(90)
print(l1)

print('-----------------------------------------------')

print('2) extend')
l1=[10,20,30]
l2=[40,50,60,70]
print(l1,l2)
l1.extend(l2)
print(l1)
l2.extend(l1)
print(l2)

print('-----------------------------------------------')

print('3) insert')
l1=[10,20,30,40,50]
print(l1)
l1.insert(2,90)
print(l1)

print('-----------------------------------------------')



print('4) pop')
l1=[10,20,30,20,40,50,20]
print(l1)
l1.pop()
print(l1)

print('-----------------------------------------------')

print('5) clear')
l1=[10,20,30,20,40,50,20]
print(l1)
l1.clear()
print(l1)

print('-----------------------------------------------')
