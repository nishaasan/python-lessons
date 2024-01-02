employees=[
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
]
employee={ 'id': 7, 'name': 'Leo' }
# def employee_is_valid(employee):
# for key in employee.items():
#   print(key)
   
id=2
print(next(e for e in employees if e['id']==id))

# for key in employee.keys():
#     print(key)
    