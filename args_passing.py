# Default values for arguments
# Help messages
# Specifying the data type of the arguments

import argparse


def convert_temperature(temp_input, scale_from, scale_to):
	if scale_from == "Celsius" and scale_to == "Fahrenheit":
		return (temp_input * 9/5) + 32
	elif scale_from == "Celsius" and scale_to == "Kelvin":
		return temp_input + 273.15
	elif scale_from == "Fahrenheit" and scale_to == "Celsius":
		return (temp_input - 32) * 5/9
	elif scale_from == "Fahrenheit" and scale_to == "Kelvin":
		return (temp_input - 32) * 5/9 + 273.15
	elif scale_from == "Kelvin" and scale_to == "Celsius":
		return temp_input - 273.15
	elif scale_from == "Kelvin" and scale_to == "Fahrenheit":
		return (temp_input - 273.15) * 9/5 + 32
	else:
		return temp_input



if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="Please enter a number first and the Celsius, Fahrenheit, or Kelvin scale FROM, and then a third argument for the scale you want to convert TO."
	)
	parser.add_argument("--temp_input", required=True, type=int)
	parser.add_argument("--scale_from", required=True, type=str)
	parser.add_argument("--scale_to", required=True, type=str)
	args = parser.parse_args()

	temp_input = args.temp_input
	scale_from = args.scale_from
	scale_to = args.scale_to

	print(convert_temperature(temp_input, scale_from, scale_to))



