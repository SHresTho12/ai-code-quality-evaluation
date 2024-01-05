from typing import List


def sort_numbers(numbers: str) -> str:
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_dict = {word: str(i) for i, word in enumerate(number_words)}
    number_list = numbers.split()
    number_list.sort(key=lambda x: int(number_dict[x]))
    return ' '.join(number_list)


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(sort_numbers): 
    assert sort_numbers('') == '' 
    assert sort_numbers('three') == 'three' 
    assert sort_numbers('three five nine') == 'three five nine' 
    assert sort_numbers('five zero four seven nine eight') == 'zero four five seven eight nine' 
    assert sort_numbers('six five four three two one zero') == 'zero one two three four five six' 
    
check(sort_numbers)