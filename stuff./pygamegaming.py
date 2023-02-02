# Define a function to perform the calculation
def calculate(x, operator, y):
  if operator == "+":
    return x + y
  elif operator == "-":
    return x - y
  elif operator == "*":
    return x * y
  elif operator == "/":
    return x / y
  else:
    return "Invalid operator"

# Get input from the user
x = int(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
y = int(input("Enter the second number: "))

# Calculate and print the result
result = calculate(x, operator, y)

# If the result is less than 5, exit the program
if result < 5:
  print("Less than 5, exiting...")
  exit()

print(result)
