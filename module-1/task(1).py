name=(input("enter your NAME : "))
if name.isalpha():
    email=(input("enter you email : "))
    if email.islower():
        password=(input("enter your password : "))
        if password.isalnum():
            cpassword=(input("enter the canformation password : "))
            if cpassword==password:
               mobileno=(input("enter your mobile number : "))
               if mobileno.isdigit():
                  id=(input("enter your id: "))
                  if id.isdigit():
                     print("your detail is varified : ")
                  else:
                     print("invalid input : ") 




   
