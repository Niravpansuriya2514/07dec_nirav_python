# bank mang.system
# 1).a/c oping
# number
# name type
# saving current

# 2)
# deposite
# -min (2000)
# 3)
# withdrwal
#  -withdraw amount is miN in 2000

# 4)statements
# num
# name 
# type 
# total balance


total=0
ACnumber=int(input("enter your acount number: "))
name=input("enter your name: ")

print("acount type-")
print("-saving\n-current")

ACtype=input("enter your acount type: ")
deposit=int(input("enter your deposit amount: "))

def deposits():

    if deposit>=2000:
        print("succesfuly")
        print(deposit)

deposits()      
withdrwals=int(input("enter your withdrwal amount: "))

if withdrwals < deposit:
    print("your withdrwal amount is",withdrwals)         
else:
    print("invalid input:")


total=deposit-withdrwals
print("your acount number",ACnumber)
print("your name",name)
print("your acount type",ACtype)
print("your total amount",total)




