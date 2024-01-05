def exchange(lst1, lst2):
    # Calculate the sum of odd numbers in lst1
    sum_odd_lst1 = sum(x for x in lst1 if x % 2 != 0)

    # Calculate the sum of odd numbers in lst2
    sum_odd_lst2 = sum(x for x in lst2 if x % 2 != 0)

    # Calculate the sum of even numbers in lst1
    sum_even_lst1 = sum(x for x in lst1 if x % 2 == 0)

    # Calculate the sum of even numbers in lst2
    sum_even_lst2 = sum(x for x in lst2 if x % 2 == 0)

    # Check if it's possible to exchange elements to make lst1 all even
    if sum_even_lst1 + sum_odd_lst2 == sum_even_lst2 + sum_odd_lst1:
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
def check(exchange):
    # Check some simple cases
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES", "Test 1"
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO", "Test 2"
    assert exchange([1, 2, 3, 4], [2, 1, 4, 3]) == "YES", "Test 3"
    assert exchange([5, 7, 3], [2, 6, 4]) == "YES", "Test 4"
    assert exchange([5, 7, 3], [2, 6, 3]) == "NO", "Test 5"
    assert exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO", "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert exchange([100, 200], [200, 200]) == "YES", "Test 7"

check(exchange)