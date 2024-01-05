def numerical_letter_grade(grades):
    """
    Convert GPAs to letter grades.

    Args:
    grades (list): List of GPAs for students.

    Returns:
    list: List of corresponding letter grades.

    Examples:
    >>> numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])
    ['A+', 'B', 'C-', 'C', 'A-']
    """

    # Initialize a list to store the letter grades
    letter_grades = []

    # Iterate through the list of GPAs
    for gpa in grades:
        # Use if-elif statements to determine the letter grade based on GPA
        if gpa == 4.0:
            letter_grades.append('A+')
        elif gpa > 3.7:
            letter_grades.append('A')
        elif gpa > 3.3:
            letter_grades.append('A-')
        elif gpa > 3.0:
            letter_grades.append('B+')
        elif gpa > 2.7:
            letter_grades.append('B')
        elif gpa > 2.3:
            letter_grades.append('B-')
        elif gpa > 2.0:
            letter_grades.append('C+')
        elif gpa > 1.7:
            letter_grades.append('C')
        elif gpa > 1.3:
            letter_grades.append('C-')
        elif gpa > 1.0:
            letter_grades.append('D+')
        elif gpa > 0.7:
            letter_grades.append('D')
        elif gpa >= 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')

    return letter_grades

def check(numerical_letter_grade):
    # Check some simple cases
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-'], "Test 1"
    assert numerical_letter_grade([1.2]) == ['D+'], "Test 2"
    assert numerical_letter_grade([0.5]) == ['D-'], "Test 3"
    assert numerical_letter_grade([0.0]) == ['E'], "Test 4"
    assert numerical_letter_grade([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+'], "Test 5"
    assert numerical_letter_grade([0, 0.7]) == ['E', 'D-'], "Test 6"

check(numerical_letter_grade)