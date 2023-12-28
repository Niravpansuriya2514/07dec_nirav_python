s1=int(input("enter your subject1 mark: "))
s2=int(input("enter your subject2 mark: "))
s3=int(input("enter your subject3 mark: "))
s4=int(input("enter your subject4 mark: "))

if s1>35 and s2>35 and s3>35 and s4>35:
    total=s1+s2+s3+s4
    print("total mark is: ",total)
    pr=total/4
    print("pr is:",pr)

    if pr>70:
        print("result: dist")
    elif pr>60:
        print("result: first class")
    elif pr>50:
        print("result: second class")
    elif pr>35:
        print("result: pass class")
else:
    print("result: 12th fail")