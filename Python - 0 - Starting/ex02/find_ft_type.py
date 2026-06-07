def all_thing_is_obj(object: any) -> int:
	classObject = object.__class__.__name__
	if (classObject == 'str'):
		print(f"{object} is in the kitchen : <class '{classObject}'>")
	elif (classObject == 'int'):
		print("Type not found")
	else:
		print(f"{classObject.capitalize()} : <class '{classObject}'>")
	return (42)
