def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                print(f"Result: {add(a, b)}")
            elif choice == 2:
                print(f"Result: {subtract(a, b)}")
            elif choice == 3:
                print(f"Result: {multiply(a, b)}")
            elif choice == 4:
                print(f"Result: {divide(a, b)}")
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid inputs.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()