def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error : Division By Zero Is Not Allowed "
    return a/b
print("===== Simple Calculator =====")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect Operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please select between 1 and 4.")
except ValueError:
    print("Invalid input! Please enter numeric values only.")
