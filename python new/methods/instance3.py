class Employee:  
  # constructor  
  department="Finance"
  def __init__(self, name,dept):  
      # Instance variable  
      self.name = name  
      self.department =dept

  # instance method to access instance variable  
  def show(self):
    print("name: ", self.name, '\n' "Department:" , self.department)

  # def new_print(self):
  #   print(f"calling instance of new_print{self}")

    def __repr__(self):
      return f"Employee(name='{self.name}', dept={self.dept})"
 
  
obj = Employee('Craig',"IT")  
obj.show() 
# obj.new_print()

print(repr(Employee))
