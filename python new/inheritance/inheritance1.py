
# A Python program to demonstrate inheritance
class Person(object):

# Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
  
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
    print("parent class called")

class emp(Person):
  def print(self):
    print(self.name, self.id)
    print("child class called")
  

# Driver code
emp = emp("John", 102) # An Object of Person
emp.print()
emp.Display()
