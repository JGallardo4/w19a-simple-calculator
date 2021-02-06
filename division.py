def divide(n1, n2):
	try:
		result = n1 / n2
	except ZeroDivisionError:
		print("You cannot divide by zero")		
	else:
		print("Your result: ", result)