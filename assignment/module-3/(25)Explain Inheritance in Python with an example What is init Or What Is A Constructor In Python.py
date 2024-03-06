# single level inheritance
class father():
    def fproperties(self):
        self.farm=int(input("how many you have in land of farm: "))
        self.balance=int(input("how many rupees in your bank: "))
        print(f"farming land:{self.farm} acre",)
        print(f"bank balance: {self.balance} rupees")
class child(father):
    def cproperties(self):
        self.bick=int(input("how many you have bicks: "))
        self.balance=int(input("how many rupees in your bank: "))
        print("bicks: ",self.bick)
        print("bank balance: ",self.balance)
obj=child()
obj.fproperties()
obj.cproperties()

# multilevel inheritance
class grandparents():
    def grandproperties(self):
        self.farm=int(input("how many you have in land of farm: "))
        self.gbalance=int(input("how many coins in silver: "))
        self.cow=int(input("how many cows: "))
class parents(grandparents):
    def prantesproperties(self):
        self.pbalance=int(input("how many bank balance: "))
        self.cars=int(input("how many cars: "))
class clild(parents):
    def childproperties(self):
        print("--------------grandparents properties---------------")
        print(f"land of farm: {self.farm} acre")
        print(f"silver coins: {self.gbalance}")
        print(f"cows: {self.cow}")
        print("--------------parents properties----------------")
        print(f"bank balance: {self.pbalance} rupees")
        print(f"cars: {self.cars}")

a=clild()
a.grandproperties()
a.prantesproperties()
a.childproperties()

# init method in Python is used to initialize objects of a class
# It is also called a constructor.
