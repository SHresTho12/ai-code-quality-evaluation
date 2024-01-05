from typing import List

def sort_numbers(numbers: str) -> str:
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_dict = {word: str(i) for i, word in enumerate(number_words)}
    number_list = numbers.split()
    number_list.sort(key=lambda x: int(number_dict[x]))
    return ' '.join(number_list)