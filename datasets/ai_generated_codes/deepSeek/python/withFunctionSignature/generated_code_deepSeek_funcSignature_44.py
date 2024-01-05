# This is a generated Python file.
def change_base(x: int, base: int):
    if x < 0:
        return '-' + change_base(-x, base)
    elif x < base:
        return "0123456789ABCDEF"[x]
    else:
        return change_base(x // base, base) + "0123456789ABCDEF"[x % base]