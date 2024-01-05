def by_length(arr):
    num_to_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
                   6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    filtered_arr = [num_to_word[i] for i in sorted(arr) if 1 <= i <= 9]
    return filtered_arr[::-1]