
import pandas as pd

def numerical_letter_grade(grades):
  """
  Converts a list of numerical grades to a list of letter grades.

  Args:
    grades: A list of numerical grades (floats).

  Returns:
    A list of letter grades (strings).
  """

  letter_grades = []
  for grade in grades:
    if grade >= 90:
      letter_grades.append("A")
    elif grade >= 80:
      letter_grades.append("B")
    elif grade >= 70:
      letter_grades.append("C")
    elif grade >= 60:
      letter_grades.append("D")
    else:
      letter_grades.append("F")
  return letter_grades

# Example usage
grades = [88, 77, 92, 65, 85]
letter_grades = numerical_letter_grade(grades)
print(letter_grades)  # Output: ['B', 'C', 'A', 'D', 'B']
