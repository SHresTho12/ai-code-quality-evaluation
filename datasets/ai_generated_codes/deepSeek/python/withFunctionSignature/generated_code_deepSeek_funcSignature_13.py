# This is a generated Python file.
def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a