

def ranges():
    n=int(input("enter your number: "))
    for i in range(100):
        if n==i:
            print("yes number is in range")
        else:
            print("no number is not in range")
            break
ranges()