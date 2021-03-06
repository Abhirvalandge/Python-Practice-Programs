# Given a non-empty string like "Code" return a string like "CCoCodCode".

# string_splosion('Code')-->'CCoCodCode'
s1='CCoCodCode'
s2=''
for x in s1:
    if x not in s2:
        s2=s2+x
print(s2)
print("------------------------------")

#string_splosion('abc')-->'aababc'
s1='aababc'
s2=''
for x in s1:
    if x not in s2:
        s2=s2+x
print(s2)
print("------------------------------")

# string_splosion('ab')-->'aab'
s1='aab'
s2=''
for x in s1:
    if x not in s2:
        s2=s2+x
print(s2)