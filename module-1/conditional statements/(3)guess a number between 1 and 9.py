

for i in range(100):
    x=int(input("enter random number between 1 to 9: "))
    if x>1 and x<9:
        print("Well guessed")
        break
    else:
        print("invalid input")