def fizz_buzz(n: int):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage
fizz_buzz(15)  # This will print the FizzBuzz sequence from 1 to 15
