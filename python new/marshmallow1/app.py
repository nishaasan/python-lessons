from marshmallow import Schema, fields
import json
# Define a simple data class for students
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Define a schema for the Student class
class StudentSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    grade = fields.Float()

# Create an instance of the Student class
student = Student(name="Alice", age=18, grade=85.5)

# Serialize the Student object using the schema
student_schema = StudentSchema()
# result_ser = student_schema.dump(student)
# result_deser=student_schema.load(result_ser)

# # Print the serialized result
# print(json.dumps(result_ser))
# print(type(result_ser))
# print()
# print(result_deser)
# print(type(result_deser))
# Serialize the Student object using the schema
result_ser = student_schema.dump(student)
print(result_ser)
print(type(result_ser))

# Convert the serialized result to a JSON string
result_ser_json = json.dumps(result_ser)

# Print the serialized result as a JSON string
print(result_ser_json)
print(type(result_ser_json))

