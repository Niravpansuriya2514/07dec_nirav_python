class account:
    import random
    
    acnumber=random.randint(111111111111,999999999999)
    def acdetail(self):
        self.name=input("enter your name: ")

class deposit:
    def deposits(self):
        self.depositamount=int(input("enter your amount: "))
        if self.depositamount>2000:
            print("successfuly")
        else:
            print("invalid input")
            print("please amount is > 2000")
        self.whithdrawwal=int(input("enter your amount: "))
        if self.whithdrawwal<self.depositamount:
            print("successfuly")
        else:
            print("invalid input")
            print("amount is < depositamount")

class prints(account,deposit):
    def print(self):
        self.total=self.depositamount-self.whithdrawwal

        print("account number: ",self.acnumber)
        print("name: ",self.name)
        print("deposit amount: ",self.depositamount)
        print("whithdrawal amount:",self.whithdrawwal)
        print("total amount: ",self.total)
obj=prints()
obj.acdetail()
obj.deposits()
obj.print()


