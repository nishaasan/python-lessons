# Python program to illustrate destructor
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')
		
    
	# Deleting (Calling destructor)
	def __repr__(self):
		return 'Employee1 created'
		
    

        
		
obj = Employee()

print(obj)
