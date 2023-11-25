# tuple1=(90,20,70)
# list1=[90,80,70]
student={"name":"Jane","lname":"kate","grade":(90,80,70,60)}
print(student["grade"])
#avg marks of the student
def marks(student):
    return sum(student["grade"])/len(student["grade"])

print(marks(student))