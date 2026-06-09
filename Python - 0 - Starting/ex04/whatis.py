import sys

def whatis(integer: int):
	"""Returns parameter of odd or even"""
	if integer % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

if __name__ == "__main__":
	try:
		if len(sys.argv) != 2:
			raise AssertionError("more than one argument is provided")
		try:
			integer = int(sys.argv[1])
		except ValueError:
			raise AssertionError("argument is not an integer")
		whatis(integer)
	except AssertionError as e:
		print(f"AssertionError: {e}")
		sys.exit(1)
