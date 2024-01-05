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
