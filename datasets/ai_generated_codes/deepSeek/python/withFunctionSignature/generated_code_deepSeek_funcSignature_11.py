# This is a generated Python file.
from typing import List

def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))