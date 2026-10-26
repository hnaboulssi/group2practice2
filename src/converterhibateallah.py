
def convert_length(value, from_unit, to_unit):
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "miles": 1609.344
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid length unit")

    if value < 0:
        raise ValueError("Value cannot be negative")

    value_in_meters = value * units[from_unit]
    result = value_in_meters / units[to_unit]

    return result
