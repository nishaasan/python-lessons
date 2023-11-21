#instance method to class method
class Student:
  marks = 0

  def compute_marks(self, obtained_marks):
    marks = obtained_marks
    print('Obtained Marks:', marks)

# convert compute_marks() to class method
Student.print_marks =classmethod(Student.compute_marks)
Student.print_marks(88)
