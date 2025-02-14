#example of some classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, {self.name}! You are {self.age} years old!")    
        
gopal = Person("Gopal Mahato",19)
gopal.greet()
dibyendu = Person("Dibyendu Garai",19)
dibyendu.greet()        

class Dog:
    def __init__(self, name,owner,sound,owner_address):
        self.name = name
        self.owner = owner
        self.sound = sound
        self.owner_address = owner_address
        
    def info(self):
        print(f"Dog Name: {self.name}\nDog Sound: {self.sound}\nDog Owner: {self.owner}\nDog Owner Address: {self.owner_address}")
        
dog1 = Dog("Puppy","Gopal Mahato","Bhow! Bhow!","L.A.,USA")
dog1.info()
dog2  = Dog("Jones","Mr. Engineer","bhook! bhook","Manchester,U.K.")
dog2.info()            
