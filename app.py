import addition
import division
import multiplication
import subtraction

class CalculatorInputError(ValueError):
	pass

def main_loop():
	print("Welcome to the simple calculator. Please select from the following options:")

	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")

	user_selection = 0

	while True:
		try:
			user_selection = int(input("Please enter your selection: "))
			if (user_selection
		< 1 or user_selection
		> 4):
				raise CalculatorInputError("Please enter a valid selection")
			else:
				break	
		except CalculatorInputError:
			continue

	while True:
		try:
			n1 = int(input("Please enter your first number: "))
			break	
		except ValueError:
			continue

	while True:
		try:
			n2 = int(input("Please enter your second number: "))
			break	
		except ValueError:
			continue

	if user_selection == 1:
		addition.add(n1, n2)

	elif user_selection == 2:
		subtraction.subtract(n1, n2)

	elif user_selection == 3:
		multiplication.multiply(n1, n2)

	elif user_selection == 4:
		division.divide(n1, n2)

	main_loop()
main_loop()