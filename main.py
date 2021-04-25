from helper.add import add
from helper.subtract import sub

class Calculator:
	def add_method(self,a,b):
		print("Result is "+str(add(a,b)))

	def sub_method(self,a,b):
		print("Result is "+str(sub(a,b)))

calc = Calculator()
calc.add_method(10,2)
calc.sub_method(10,2)

