class circle():
    def areaofcircle(self):
        self.radius=float(input("enter your radius: "))
        self.pi=3.14
        print("area of circle is: ",self.pi*self.radius*self.radius)
        print("circle perimeter is: ",2*self.pi*self.radius)

a=circle()
a.areaofcircle()