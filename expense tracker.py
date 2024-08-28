import json

# File to store expenses
FILE_NAME = 'expenses.json'

def load_expenses():
    """Load expenses from the JSON file."""
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense."""
    description = input("Enter the expense description: ")
    amount = float(input("Enter the expense amount: "))
    expense = {"description": description, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    """View all expenses."""
    if not expenses:
        print("No expenses found.")
        return
    print("\nExpenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Description: {expense['description']}, Amount: ${expense['amount']:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
