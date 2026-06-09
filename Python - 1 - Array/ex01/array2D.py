def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints 2D list shape and returns a truncated version using slicing.
    """

    if not isinstance(family, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("Input must be a 2D list (list of lists).")

    rows = len(family)
    cols = len(family[0]) if rows > 0 else 0

    if not all(len(row) == cols for row in family):
        raise ValueError("All rows in the 2D array must be same size.")

    print(f"My shape is : ({rows}, {cols})")

    new_family = family[start:end]

    new_rows = len(new_family)
    new_cols = len(new_family[0]) if new_rows > 0 else 0

    print(f"My new shape is : ({new_rows}, {new_cols})")

    return new_family
