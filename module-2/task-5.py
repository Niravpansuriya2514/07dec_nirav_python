class account:
    import random
    accountno=random.randint(111111111111,999999999999)
    name=""
    def accountopaning(self):
        self.name=input("enter your name: ")
class deposite(account):
    depositeam=0
    def deposites(self):
        self.depositeam=int(input("enter your amount: "))
        if self.depositeam>2000:
            print("sucksesfully")
        else:
            print("please enter min amount = 2000")
class withdrawals(deposite):
    withdrawal=0
    def withdrawalam(self):
        self.withdrawal=int(input("enter your withdrawal amount: "))
        if self.withdrawal<self.depositeam:
            print("suckssesfully")
        else:
            print("please enter amount less than deposite amount")
class statements(withdrawals):
    def statement(self):
        print("name: ",self.name)
        print("account no: ",self.accountno)
        print("deposite amount: ",self.depositeam)
        print("withdrawal amount: ",self.withdrawal)
        print("tatal balance: ",self.depositeam-self.withdrawal)

obj=statements()
obj.accountopaning()
obj.deposites()
obj.withdrawalam()
obj.statement()

