def by_length(arr):
    num_to_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
                   6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    filtered_arr = [num_to_word[i] for i in sorted(arr) if 1 <= i <= 9]
    return filtered_arr[::-1]


def check(by_length):
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert by_length([]) == [], "Error"
    assert by_length([1, -1 , 55]) == ['One'], "Error"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails 2 (also good for debugging!)"
assert by_length([1, -1, 3, 2]) == ["Three", "Two", "One"]
assert by_length([9, 4, 8]) == ["Nine", "Eight", "Four"]

check(by_length)