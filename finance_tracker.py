def add_expense (data):
    expenseDescription = input("Enter expense description: ")
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Must enter valid amount! ")
    else:
        if amount < 0:
            raise ValueError("Amount cannot be negative! ")
        else:
            if category not in data:
                data[category] = []
            data[category].append((expenseDescription, amount))
            print("Expense added!")

def view_summary (data):
    for category in data:
        total = 0
        for desc, price in data[category]:
            total += price
        print(f"Total spent on {category}: ${total:.2f}")

def view_expenses (data):
    for category in data:
        print(f"Category: {category}")
        for desc, price, in data[category]:
            print(f" - {desc}: ${price:.2f}")

finances = {}
command = 0

print("Welcome to the personal finances tracker!")
while command != 4:
    command = int(input("What would you like to do? \n 1. Add Expense \n 2. View All Expenses \n 3. View Summary \n 4. Exit \n Choose a number: "))
    if command <= 0 or command > 4:
        raise ValueError("Must enter valid command number!")
    else:
        if command == 1:
            add_expense(finances)
        elif command == 2:
            if not finances:
                print("You have no expenses to view.")
            else:
                view_expenses(finances)
        elif command == 3:
            if not finances:
                print("You have no expenses to summarize.")
            else:
                view_summary(finances)
        elif command == 4:
            print("Thank you for using the personal finance tracker!")

