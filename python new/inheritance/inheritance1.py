class Person():

# Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
  
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
    print("parent class called")

# p1=Person("Bala",1)
# p1.Display()

class emp(Person):
    
    def __init__(self, name, id, employee_id):
        super().__init__(name, id)  
        self.employee_id = employee_id  
    def print(self):
        print(self.name, self.id, self.employee_id)
        print("child class called")
        
    def is_employee(self):
      if self.id == self.employee_id:
        return True
      else:
        return False


emp_obj = emp("John", 102, 1002)  
emp_obj.print()
emp_obj.Display()  
print(emp_obj.is_employee())
