def count_nums(arr):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sum(1 for num in arr if sum_of_digits(num) > 0)