class print_new:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    self.course="python"
   
    

a=print_new("john",25)
print(a.name,a.age,a.course)


class Student:
  def __init__(self,name,age,course):
    self.name=name
    self.age=age
    self.course="python"    

  def __str__(self):
    return "name: "+self.name+" age: "+str(self.age)+" course: "+self.course

  


s=Student("nisha",25,"python")
print(s)

s1=Student("Bob")
s2=Student("Jack",(90,30,40))
print(s2.name)
print(s2.name)
print(s1.grades)
print(s2.avg())


class Person():
  def __int__(self,name,age):
    self.name=name
    self.age=age

p1=Person("John",25)