def pluck(arr, key):
    return [d.get(key, None) for d in arr]
