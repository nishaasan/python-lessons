class Car:
    def __init__(self, make, model, year,name):
        self.__make = make   # private variable
        self.__model = model # private variable
        self.__year = year 
        self.name=name  

    # Getter method
    def get_make(self):
        return self.__make
    
    # Setter method
    def set_make(self, make):
        self.__make = make

# Usage
my_car = Car("Toyota", "Corolla", 2020,"car1")
print(my_car.get_make()) # Accessing private variable via getter
my_car.set_make("Honda") # Modifying private variable via setter
print(my_car.get_make())
print(my_car.name)
# print(my_car.__make)