from typing import List


def sort_numbers(numbers: str) -> str:
    # Split the string into a list of numbers
    number_list = numbers.split()

    # Convert each number in the list to an integer
    number_list = [int(num) for num in number_list]

    # Sort the list of numbers
    number_list.sort()

    # Convert the sorted numbers back to strings and join them into a single string
    return ' '.join(map(str, number_list))

# Example usage
test_numbers = "3 1 4 1 5 9 2 6 5 3 5"
result = sort_numbers(test_numbers)
result

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(sort_numbers): 
    assert sort_numbers('') == '' 
    assert sort_numbers('three') == 'three' 
    assert sort_numbers('three five nine') == 'three five nine' 
    assert sort_numbers('five zero four seven nine eight') == 'zero four five seven eight nine' 
    assert sort_numbers('six five four three two one zero') == 'zero one two three four five six' 
    
check(sort_numbers)