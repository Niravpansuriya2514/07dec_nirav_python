
def palidrome():
    n=input("enter your string: ")
    a=n[::-1]
    if a==n:
        print("string is palidrom")
    else:
        print("string is not palidrom")

palidrome()