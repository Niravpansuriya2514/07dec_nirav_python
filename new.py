try:
  name=(input("enter your NAME : "))
  if name.isalpha():
    print("succses")
  else:
    print("invalid input")
    raise ValueError
except:
    print("error")
  
else:
  phone=input("enter your number: ")
  if phone.isdigit():
    if len(phone)==10:
      print("suckess")
    else:
      print("invalid input")


    # email=(input("enter you email : "))
    # if email.islower():
    #     password=(input("enter your password : "))
    #     if password.isalnum():
    #         cpassword=(input("enter the canformation password : "))
    #         if cpassword==password:
    #            mobileno=(input("enter your mobile number : "))
    #            if mobileno.isdigit():
    #               id=(input("enter your id: "))
    #               if id.isdigit():
                     