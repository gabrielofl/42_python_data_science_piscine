import sys

def whatis(integer: int):
	if integer % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		try:
			integer = int(sys.argv[1])
			whatis(integer)
		except:
			# raise AssertionError("argument is not an integer")
			print("AssertionError: argument is not an integer")
	else:
		if len(sys.argv) > 1:
			# raise AssertionError("more than one argument is provided")
			print("AssertionError: more than one argument is provided")
