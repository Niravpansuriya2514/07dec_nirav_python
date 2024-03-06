
# self is  default arguments

class studinfo:
    stid=7238
    stnm='nirav'


    def getdata(self):
        print("This is getdata!")
    
    def getsum(self,a,b):
        print("Sum:",a+b)
a=studinfo()
a.getdata()
a.getsum(22,43)