def pluck(arr):
    even_values = [(i, val) for i, val in enumerate(arr) if val % 2 == 0]
    if not even_values:
        return []
    else:
        smallest_even_value = min(even_values, key=lambda x: (x[1], x[0]))
        return list(smallest_even_value)