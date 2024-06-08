class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof! My name is {} and I am {} years old.".format(self.name, self.age))

    def __repr__(self):
        return f"{self.name} is called"
    
    

        

    


dog1=Dog("woofy",5)

dog1.bark()

dog2=Dog("black",6)
dog2.bark()
print(dog1)
print(dog2)