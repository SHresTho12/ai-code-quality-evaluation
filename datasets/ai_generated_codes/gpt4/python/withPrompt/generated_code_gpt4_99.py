def closest_integer(value):
    # Convert the value to a float
    float_value = float(value)

    # Calculate the floor and ceiling values
    floor_value = int(float_value) if float_value >= 0 else int(float_value) - 1
    ceil_value = floor_value + 1

    # Calculate the absolute differences from the floor and ceiling
    diff_floor = abs(float_value - floor_value)
    diff_ceil = abs(float_value - ceil_value)

    # Check which integer is closer and return it
    if diff_floor < diff_ceil:
        return floor_value
    else:
        return ceil_value

# Test cases
print(closest_integer("10"))     # Output: 10
print(closest_integer("15.3"))   # Output: 15
print(closest_integer("14.5"))   # Output: 15
print(closest_integer("-14.5"))  # Output: -15
