class student:
    
    def __init__(self,name,contact,roll):
        self.name = name
        self.contact = contact
        self.roll = roll
        
    def doSomething(self):
        print(f"student {self.roll} is doing something")
    
    
s1 = student("amey",9766696550,1)

print(s1.name)
print(s1.contact)
print(s1.roll)

s1.doSomething()