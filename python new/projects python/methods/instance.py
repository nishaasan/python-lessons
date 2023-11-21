class Student:
  def __init__(self,name,age,course):
    self.name=name
    self.age=age
    self.course="python"    

  def __str__(self):
    return "name: "+self.name+" age: "+str(self.age)+" course: "+self.course
    print("hello")

  def avg(self):
    return sum(self.grades)/len(self.grades)


s=Student("nisha",25,"python")
print(s)

s1=Student("Bob")
s2=Student("Jack",25,(90,30,40))
print(s2.name)