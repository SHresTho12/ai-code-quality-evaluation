def exchange(lst1, lst2):
    odd_in_lst1 = sum(1 for num in lst1 if num % 2 != 0)
    even_in_lst2 = sum(1 for num in lst2 if num % 2 == 0)

    return "YES" if odd_in_lst1 <= even_in_lst2 else "NO"