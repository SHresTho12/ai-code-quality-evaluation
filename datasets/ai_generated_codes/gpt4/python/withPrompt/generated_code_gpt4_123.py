def get_odd_collatz(n):
    # Initialize an empty list to store the odd numbers in the Collatz sequence
    odd_collatz = []
    
    # Define the Collatz sequence function
    def collatz_sequence(num):
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            sequence.append(num)
        return sequence
    
    # Generate the Collatz sequence for the given number n
    collatz_seq = collatz_sequence(n)
    
    # Iterate through the sequence and add odd numbers to the list
    for num in collatz_seq:
        if num % 2 == 1:
            odd_collatz.append(num)
    
    # Sort the list in increasing order
    odd_collatz.sort()
    
    return odd_collatz

# Test case
print(get_odd_collatz(5))  # Output: [1, 5]
