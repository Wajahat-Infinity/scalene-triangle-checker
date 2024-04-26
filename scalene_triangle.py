def is_scalene_triangle(side1, side2, side3):
  """
  This function determines if a triangle is scalene based on its side lengths.

  Args:
      side1 (float): Length of the first side.
      side2 (float): Length of the second side.
      side3 (float): Length of the third side.

  Returns:
      bool: True if the triangle is scalene, False otherwise.
  """

  # Check if any side length is greater than the sum of the other two.
  # If so, the triangle inequality is violated, and it cannot be a triangle.
  if (side1 > side2 + side3) or (side2 > side1 + side3) or (side3 > side1 + side2):
    return False

  # Check if all sides are different lengths.
  return side1 != side2 and side1 != side3 and side2 != side3

# Get user input for side lengths
try:
  side1 = float(input("Enter the length of the first side: "))
  side2 = float(input("Enter the length of the second side: "))
  side3 = float(input("Enter the length of the third side: "))
except ValueError:
  print("Invalid input. Please enter numbers only.")
  exit()

# Check if the triangle is scalene
if is_scalene_triangle(side1, side2, side3):
  print("The triangle is scalene.")
else:
  print("The triangle is not scalene.")
