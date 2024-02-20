# class print_new:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#     self.course="python"
   
    

# a=print_new("john",25)
# print(a.name,a.age,a.course)


class Student:
  def __init__(self,name,age,course):
    self.name=name
    self.age=age
    self.course="nfhfa"

  def __str__(self):
    return "name: "+self.name+" age: "+str(self.age)+" course: "+self.course

  def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, course='{self.course}')"

  def name_new(self,name1):
    self.name1=name1
    print(self.name1)


s=Student("nisha",25,"python")
print(s)
print(repr(s))  # Output: Student(name='nisha', age=25, course='python')
s.name_new("bala")

s1=Student("Bob",23,"Java")
print(s1)



# s2=Student("Jack",(90,30,40))
# print(s2.name)
# print(s2.name)
# print(s1.grades)
# print(s2.avg())

# #demo methods
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age})"

#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"

# # Example usage
# p1 = Person("John", 25)

# # __repr__ method will be called when using repr() or printing the object directly
# print(repr(p1))  # Output: Person(name='John', age=25)

# # __str__ method will be called when using str() or printing the object directly
# print(str(p1))   # Output: Name: John, Age: 25
