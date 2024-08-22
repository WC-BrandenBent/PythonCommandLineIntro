import sys

def print_input(user_input):
	print(user_input)

if __name__ == "__main__":
  print_input(sys.argv[2])
 

# argsv is a list of strings representing the arguments passed to the script -> "args Vector"

# The main method in Python is the entry point for a Python program. It's the first function that's executed when the script is run directly. The main method is defined by checking the __name__ variable. If the __name__ variable is set to __main__, then the main method is executed. If the __name__ variable is set to something else, then the main method is not executed.

# In Python, __name__ is a special variable assigned to the name of the Python module by the interpreter. If your module is invoked as a script, then the string ‘__main__’ will automatically be assigned to the special variable __name__. But if you import your module into another module, the string ‘my_module’ will be assigned to __name__