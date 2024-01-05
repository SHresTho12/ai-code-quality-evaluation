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
