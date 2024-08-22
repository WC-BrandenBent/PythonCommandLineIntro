import sys

def celsius_to_fahrenheit(celsius):
	fahrenheit = (celsius * 9/5) + 32
	return fahrenheit

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python temp_calc.py <temperature>")
		sys.exit(1)

	try:
		celsius = float(sys.argv[1])
		fahrenheit = celsius_to_fahrenheit(celsius)
		print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
	except ValueError:
		print("Invalid temperature value. Please enter a valid number.")