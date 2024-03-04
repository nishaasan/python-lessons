from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def sound(self):
        return "I am an animal"

class Dog(Animal):
    def sound(self):
        return "Bow!!Bow!!"
    

class Cat(Animal):
    def sound(self):
        return "Meow!!Meow!!"
    
dog=Dog("Tom")
cat=Cat("kitty")
# animal=Animal("ani")

# print(animal.sound())  
print(dog.name ,"says", dog.sound())