def calculator():
    print("=== Simple Calculator ===")
    while True:
        print("\nChoose operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "5":
            print("Exiting calculator...")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", num1 + num2)
            elif choice == "2":
                print("Result:", num1 - num2)
            elif choice == "3":
                print("Result:", num1 * num2)
            elif choice == "4":
                print("Result:", num1 / num2)
            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Enter numbers only.")
        except ZeroDivisionError:
            print("Cannot divide by zero!")

if __name__ == "__main__":
    calculator()