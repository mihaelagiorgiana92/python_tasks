
def main():
    expenses = []

    while True:
        print("What would you like to do?")
        print("1. Add an Expense")
        print("2. Show Summary")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Function to add an expense
def add_expense(expenses):
    print("\n--- Add an Expense ---")
    try:
        amount = float(input("Enter the amount: £"))
        if amount <= 0:
            print("Expense amount must be greater than 0.\n")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")
        return

    category = input("Enter the category: ").strip()
    description = input("Enter a description: ").strip()
    expenses.append({"amount": amount, "category": category, "description": description})
    print(f"Added: £{amount:.2f} for {category} ({description}).\n")

def show_summary(expenses):
    print("\n--- Expense Summary ---")
    
    if not expenses:
        print("No expenses recorded.\n")
        return

    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: £{total:.2f}")
    for expense in expenses:
        print(f"{expense['category']}: £{expense['amount']:.2f} ({expense['description']})")

main()


