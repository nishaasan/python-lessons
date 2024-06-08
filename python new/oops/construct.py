class GeekforGeeks:

	# default constructor
	def __init__(self,name):
		self.geek = "GeekforGeeks"
		self.__name=name

	# a method for printing data members
	def print_Geek(self):
		print(f"{self.__name}")


# creating object of the class
obj = GeekforGeeks("nisha")

# calling the instance method using the object obj
obj.print_Geek()
