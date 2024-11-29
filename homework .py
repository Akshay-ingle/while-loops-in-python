# Function to count the digits in a number
def count_digits(number):
    # Convert the number to a string to handle digits
    # Use abs() to handle negative numbers
    number = abs(number)
    digit_count = 0

    # Count digits
    while number > 0:
        number //= 10  # Remove the last digit
        digit_count += 1

    return digit_count

# Input from the user
try:
    num = int(input("Enter a number: "))
    if num == 0:
        print("The number 0 has 1 digit.")
    else:
        print(f"The number {num} has {count_digits(num)} digits.")
except ValueError:
    print("Please enter a valid integer.")
