class vehical: 
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def move(self):{
        print("moving !")   
    }
    
class car(vehical):
    def __init__(self, name, type):
        super().__init__(name, type)
    
    def move(self):{
        print(f"car is driving")
    }
    
class boat(vehical):
    def __init__(self, name, type):
        super().__init__(name, type)
        
    def move(self):{
        print(f"boat is sailing")
    }
    
    
c1 = car("audi","petrol")
b1 = boat("my boat","petrol")

c1.move()
b1.move()

for object in (c1,b1):
    object.move()