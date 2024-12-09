class parent:

    data  = 10

    def __init__(self,name):
        self.name = name

    def intro(self):
        print(f"{self.name} hello !")    
        
class child(parent):
    
    def __init__(self, name):
        super().__init__(name)


childObject = child("amey")

print(childObject.data)

childObject.intro()