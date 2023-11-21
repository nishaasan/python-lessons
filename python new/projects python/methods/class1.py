
class Student:
  school_name = 'ABC School'

  def __init__(self, name, age):
      self.name = name
      self.age = age

  def show(self):
      print(self.name, self.age)

# class ended

# method outside class(class method)
def exercises(cls):
  # access class variables
  print("Below exercises for", cls.school_name)

# Adding class method at runtime to class
Student.exercises = classmethod(exercises)

jessa = Student("Jessa", 14)
jessa.show()
# call the new method
Student.exercises()