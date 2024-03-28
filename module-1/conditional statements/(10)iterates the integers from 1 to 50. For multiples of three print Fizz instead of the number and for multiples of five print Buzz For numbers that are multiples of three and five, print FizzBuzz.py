for i in range(1,50):
    if i%3==0:
        print("fizz",i)
        continue
    elif i%5==0:
        print("buzz",i)
        continue
    elif i%3==0 and i%5==0:
        print("fizzbuzz",i)
        continue
    else:
        print(i)

