def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculates BMI from lists of heights and weights."""

    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Inputs must be lists.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size.")

    bmi_list = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("All elements must be integers or floats.")

        if h <= 0:
            raise ValueError("Height must be greater than zero.")

        bmi_list.append(w / (h ** 2))

    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of booleans: True if the BMI is above the limit."""

    if not isinstance(bmi, list):
        raise TypeError("BMI input must be a list.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")

    result = []
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("All elements must be integers or floats.")
        result.append(b > limit)

    return result
