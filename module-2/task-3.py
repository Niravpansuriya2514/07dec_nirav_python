# def getdata():
#     id=(input("enter your id: "))
#     name=input("enter your name: ")
#     sub=input("enter your name: ")

#     print(id)
#     print(name)
#     print(sub)



# def fun(id,name,sub):
#     print(id,name,sub)


# if n=='+':
#         print(a+b)
# elif n=='-':
#         print(a-b)
# elif n=='*':
#         print(a*b)
# elif n=='/':
#         print(a/b)
# else:
    # print("invalid input")


   
for i in range(5):
      a=int(input("enter your number: "))
      b=int(input("enter your number: "))


      print("press + add")
      print("press - sub")
      print("press * mul")
      print("press / div")
      print("no more opreration any any key:")  
      n=input("enter your choice:")

    
      def add():
           print(a+b)
      def sub():
        print(a-b)
      def mul():
        print(a*b)
      def div():
        print(a/b)


      if n=='+':
           add()
      elif n=='-':
           sub()
      elif n=='*':
           mul()
      elif n=='/':
           div()
      else:
        break
        
        print("invalid input")

