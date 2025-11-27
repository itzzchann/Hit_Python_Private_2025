class Manufacturer:
    def __init__(self,identify,location):
        self.identify=identify
        self.location=location
    def describe(self)->None:
        print(f"Identify: {self.identify}-location: {self.location}")

class Device:
    def __init__(self,name,price,identify,location):
        self.name=name
        self.price=price
        self.Manufacturer=Manufacturer(identify,location)
    def describe(self)-> None:
        print(f"Name:{self.name}-price:{self.price}",end=" ")
        self.Manufacturer.describe()
device1 = Device(name="mouse", price=2.5, identify=9725, location="Vietnam")
device1.describe()
device2 = Device(name="monitor", price=12.5, identify=11, location="Germany") 
device2.describe()
