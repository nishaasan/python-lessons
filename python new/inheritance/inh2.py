
# parent class
class Person(object):

  # __init__ is known as the constructor
  def __init__(self, name, idnumber):
    self.name = name
    self.idnumber = idnumber

  def display(self):
    print(self.name)
    print(self.idnumber)

# child class
class Employee(Person):
  def __init__(self, name, idnumber, salary, post):
    self.salary = salary
    self.post = post
    super().__init__("john",1)

  def emp_disp(self):
    print(self.name,self.idnumber,self.salary,self.post)

  
  

# creation of an object variable or an instance
a = Employee('Rahul', 886012,20000,"intern")

# calling a function of the class Person using its instance
a.display()
a.emp_disp()

