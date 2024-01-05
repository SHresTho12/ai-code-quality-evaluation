def numerical_letter_grade(grades):
    letter_grades = []

    for grade in grades:
        if 90 <= grade <= 100:
            letter_grades.append('A')
        elif 80 <= grade < 90:
            letter_grades.append('B')
        elif 70 <= grade < 80:
            letter_grades.append('C')
        elif 60 <= grade < 70:
            letter_grades.append('D')
        else:
            letter_grades.append('F')

    return letter_grades

# Example usage
print(numerical_letter_grade([92, 85, 73, 67, 58]))  # Output: ['A', 'B', 'C', 'D', 'F']


def check(numerical_letter_grade):
    # Check some simple cases
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-'], "Test 1"
    assert numerical_letter_grade([1.2]) == ['D+'], "Test 2"
    assert numerical_letter_grade([0.5]) == ['D-'], "Test 3"
    assert numerical_letter_grade([0.0]) == ['E'], "Test 4"
    assert numerical_letter_grade([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+'], "Test 5"
    assert numerical_letter_grade([0, 0.7]) == ['E', 'D-'], "Test 6"

check(numerical_letter_grade)