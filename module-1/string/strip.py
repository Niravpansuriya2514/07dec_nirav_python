# a=input("enter your value: ")
a="i am nIrAv"
print(a.strip())

# your string convert to small alphabet
print(a.lower())

# your string convert to capital alphabet
print(a.upper())

# your string replace to any character or sub string
print(a.replace('i','I'))
print(a.replace('i','not'))
print(a.replace('am','not'))

# your string convert to first character in capital
print(a.capitalize())

# your string convert to small alphabet
print(a.casefold())

# your string count charecter or sub string
print(a.count('i'))
print(a.count('am'))

# your string check end and return true and false
print(a.endswith('!'))

# your string check start and return true and false
print(a.startswith('i'))

#your string find index in any character and sub string 
print(a.find('am'))
print(a.find('m'))

#your string find index in any character and sub strin
print(a.index('am'))
print(a.index('m'))

#check your string is alphabet
print(a.isalpha())

#check your string is digit
print(a.isdigit())

#check your string is alpha and numeric
print(a.isalnum())

#check your string is small alphabet
print(a.islower())

#check your string is capital alphabet
print(a.isupper())

# your string is convert to all sub string first character is capital
print(a.title())