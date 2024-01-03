n=int(input("how many student are data in enter:"))
list=['id','name','city']
data={}


for i in range(n):
    subdata=input("enter your student name: ")
    data[subdata]={}

    id=input("enter your id: ")
    city=input("enter your city: ")
    phone=input("enter your phone number: ")

    data[subdata]["id"]=id
    data[subdata]["city"]=city
    data[subdata]["phone no"]=phone
    
print(data)
    

