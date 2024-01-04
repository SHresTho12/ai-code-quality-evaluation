
from collections import Counter

def fruit_distribution(s, n):
  """
  Calculates the distribution of fruits in a string with n baskets.

  Args:
      s: The string containing fruits represented by characters (str).
      n: The number of baskets available (int).

  Returns:
      A dictionary mapping each fruit character to its assigned basket (dict).
  """

  # Create a counter to track fruit occurrences
  fruit_counts = Counter(s)

  # Calculate the number of fruits per basket
  fruits_per_basket = len(fruit_counts) // n

  # Initialize an empty dictionary to store fruit distribution
  fruit_distribution = {}

  # Assign fruits to baskets based on their count and the number of baskets
  for fruit, count in fruit_counts.items():
    # Calculate the number of baskets needed for this fruit
    baskets_needed = count // fruits_per_basket

    # Assign the remaining fruits to the next available basket
    remaining_fruits = count % fruits_per_basket

    for i in range(baskets_needed + 1):
      fruit_distribution[fruit] = i + 1
      if remaining_fruits > 0:
        remaining_fruits -= 1

  return fruit_distribution

# Example usage
fruit_string = "aabbbcccdddeeeeffffggg"
number_of_baskets = 3

fruit_distribution = fruit_distribution(fruit_string, number_of_baskets)

print("Fruit distribution:")
for fruit, basket in fruit_distribution.items():
  print(f"- {fruit}: Basket {basket}")
