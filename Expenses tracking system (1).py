username = "admin"
password = "1234"

attempts = 3

while attempts > 0:

    print("\n=== PERSONAL EXPENSE TRACKER SYSTEM ===")

    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    if user == username and pwd == password:

        print("Login Successful!")

        expenses = []

        while True:

            print("\n--- MENU ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Show Total Expense")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                item = input("Enter expense name: ")
                amount = float(input("Enter amount: "))

                expenses.append([item, amount])

                print("Expense added successfully!")

            elif choice == "2":

                if len(expenses) == 0:
                    print("No expenses recorded.")

                else:
                    print("\nExpenses List:")

                    for i, expense in enumerate(expenses, start=1):
                        print(f"{i}. {expense[0]} - ${expense[1]:.2f}")

            elif choice == "3":

                total = 0

                for expense in expenses:
                    total += expense[1]

                print(f"Total Expenses: ${total:.2f}")

            elif choice == "4":
                print("Thank you for using the Expense Tracker.")
                break

            else:
                print("Invalid choice. Please try again.")

        break

    else:
        attempts -= 1
        print(f"Invalid username or password. Attempts left: {attempts}")

if attempts == 0:
    print("Access Denied. Too many failed login attempts.")    


