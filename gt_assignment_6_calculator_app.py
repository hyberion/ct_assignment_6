#CT Assignment 6: Calculator App Part 1: The Onening.
# Build a basic calculator app that can perform the following operations: addition, subtraction, multiplication, and division.
# The app should take in two numbers and an operator, and then it should return the result.
# The emperor protects.
#********************************************VERSON ONE***********************************************************************

# Addition
def add(x, y):
    return x + y
# Subtraction
def subtract(x, y):
    return x - y
# Multiplication
def multiply(x, y):
    return x * y
# Division
def divide(x, y):
    if y==0:
        return "Error! You can't divide by zero. That's just silly"
    return x / y

# User input

def get_operation():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Find the square root of -1")
    choice = input("Enter choice(1/2/3/4/5):")
    return choice

# Get the voodoo
def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Please enter a valid number.  The authorities have been notified.")
        return None, None
    
# Doo the voodoo

def calculator():
    while True:
        choice = get_operation()
        # If no choice was made, something must happen
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Your deviant behaviour has been logged")
        # if 5 is chosen, the universe will break, we should warn them.
        if choice == '5':
            print("Nice try.  You know that showing that result would break the universe.  Try again.")
            continue
        # If a valid choice is made, get the numbers and do the math.  It would only be polite really.
        if choice in ['1', '2', '3', '4', '5']:
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                continue
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        # If they choose to do something else, we should let them know that they are being watched.
        else:
            print("Your request was not valid.  Please remain seated until the caclulator police arrive.")
            print("Assume the position.")
        
        another_calculation = input("Do you want to do another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            print("Thank you for using our calculator. Your bio-metrics have been recorded.")
            break

#Run the calculator
calculator()