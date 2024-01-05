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
