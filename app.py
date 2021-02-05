import addition
import division
import multiplication
import subtraction

class CalculatorInputError(ValueError):
	pass

def main_loop():
	print("Welcome to the simple calculator. Please select from the following options:")

	print()

	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")

	print()

	user_selection = 0

	while True:
		try:
			user_selection = int(input("Please enter your selection: "))
			print()
			if (user_selection < 1 or user_selection > 4):
				raise CalculatorInputError("**Please enter a valid option**\n")
			else:
				break
		except CalculatorInputError as err:
			print(err)
			continue
		except ValueError:
			print("\n**Please enter an integer**\n")
			continue		

	while True:
		try:
			n1 = int(input("Please enter your first number: "))
			print()
			break	
		except ValueError:
			print("\n**Please enter a valid number**\n")
			continue

	while True:
		try:
			n2 = int(input("Please enter your second number: "))
			print()
			break	
		except ValueError:
			print("\n**Please enter a valid number**\n")
			continue

	if user_selection == 1:
		addition.add(n1, n2)

	elif user_selection == 2:
		subtraction.subtract(n1, n2)

	elif user_selection == 3:
		multiplication.multiply(n1, n2)

	elif user_selection == 4:
		division.divide(n1, n2)

	print()

	while True:
		try:
			response = input("Would you like to perform a new operation (y/n): ")
			if (response != "y" and response != "n"):
				raise CalculatorInputError("\n**Please enter a valid option**\n")
			else:
				if (response == "y"):
					print("\n**\n")		
					main_loop()
				else:
					break	
		except CalculatorInputError as err:
			print(err)
			continue
	
main_loop()