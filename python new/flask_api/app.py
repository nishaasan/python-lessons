
import json
from flask import Flask, jsonify, request
app = Flask(__name__)

employees = [
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
]
 

nextEmployeeId = 4

@app.route('/employees', methods=['GET'])
def get_employees():
 return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
 employee = get_employee(id)
 if employee is None:
   return jsonify({ 'error': 'Employee does not exist'}), 404
 return jsonify(employee)

def get_employee(id):
 return next((e for e in employees if e['id'] == id), None)


def employee_is_valid(employee):
  for key in employee.keys():
    if key != 'name':
 	    return False
 

@app.route('/employees', methods=['POST'])
def create_employee():
 employee=request.json
 print(employee)
 
 employees.append(employee)
 return employees

 
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee_by_id(id: int):
 employee = get_employee(id)
 if employee is None:
   return jsonify({ 'error': 'Employee does not exist'}), 404
 updated_employee=request.json
 employee.update(updated_employee)
 return employee



@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
 global employees
 employee = get_employee(id)
 if employee is None:
   return jsonify({ 'error': 'Employee does not exist.' }), 404

 employees = [e for e in employees if e['id'] != id]
 return jsonify(employee), 200

if __name__ == '__main__':
   app.run(debug=True,port=2000)