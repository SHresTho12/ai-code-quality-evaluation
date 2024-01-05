# This is a generated Python file.
def derivative(xs: list):
    return [xs[i] - xs[i - 1] for i in range(1, len(xs))]