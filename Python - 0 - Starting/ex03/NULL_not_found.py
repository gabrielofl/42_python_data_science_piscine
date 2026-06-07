def NULL_not_found(object: any) -> int:
    class_name = object.__class__.__name__

    if object is None:
        print(f"Nothing: None <class '{class_name}'>")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: nan <class '{class_name}'>")
    elif object == "":
        print(f"Empty: <class '{class_name}'>")
    elif class_name == 'bool':
        print(f"Fake: {object} <class '{class_name}'>")
    elif class_name == 'int':
        print(f"Zero: {object} <class '{class_name}'>")
    else:
        print("Type not Found")
        return 1
        
    return 0