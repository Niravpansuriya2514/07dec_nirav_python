try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b+c)
except NameError:
    print("Error!")
except ValueError:
    print("invalid input")