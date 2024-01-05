def string_xor(a: str, b: str) -> str:
    # Find the length of the longer string
    max_length = max(len(a), len(b))
    
    # Extend both strings to the length of the longer string, using '\x00' (null character) as padding
    a = a.ljust(max_length, '\x00')
    b = b.ljust(max_length, '\x00')

    # Perform XOR operation character by character and build the result string
    result = ''.join(chr(ord(char_a) ^ ord(char_b)) for char_a, char_b in zip(a, b))

    return result
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(string_xor): 
    assert string_xor('111000', '101010') == '010010' 
    assert string_xor('1', '1') == '0' 
    assert string_xor('0101', '0000') == '0101' 
    
check(string_xor)