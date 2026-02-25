import json

import os
from datetime import datetime



FILENAME="expenses.json"

#Utility function

def load_expenses():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_expenses(expenses):
    with open(FILENAME,"w") as f:
        json.dump(expenses,f,indent=4)


def add_expenses(expenses):
    try:
        date = input("Enter date(DD-MM-YYYY) or press Enter for today: ")
        if not date:
            date=datetime.today().strftime("%d-%m-%Y")

        category = input("Enter category (Food, Travel, etc): ").strip()
        if not category:
            category="Not Disclosed"
        description = input("Enter description: ").strip()
        if not description:
            description="Not Disclosed"
        amount = float(input("Enter amount: "))

        if amount<=0:
            raise ValueError("Amount Must be Positive")

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount

        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")
    except ValueError as e:
        print("invalid Input: ",e)
def view_expenses(expenses):
    if not expenses:
        print("No Expense Found")
        return
    print("\n---------All Expenses----------")
    for i,exp in enumerate(expenses,start=1):
        print(f"{i}. {exp['date']} |  {exp['category']}  | {exp['description']} | {exp['amount']} ")

def summarise_expenses(expenses):
    if not expenses:
        print("No  Expenses to Summarize.")
        return
    total = sum(exp['amount'] for exp in expenses)
    category_totals ={}

    for exp in expenses:
        category=exp['category']
        category_totals[category]=category_totals.get(category,0)+exp["amount"]

    print("\n------ Summary ------")
    print(f"Total Expense: ₹{total}")

    print("\nCategory-wise Breakdown:")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount}")
def delete_expense(expenses):
    view_expenses(expenses)
    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses(expenses)
            print("Deleted:", removed["description"])
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")


def generate_html_report(expenses):
    if not expenses:
        print("No expenses to generate report.")
        return

    html_content = """
    <html>
    <head>
        <title>Expense Report</title>
        <style>
            body { font-family: Arial; padding: 20px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
            th { background-color: #f4f4f4; }
        </style>
    </head>
    <body>
        <h1>Expense Summary Report</h1>
        <table>
            <tr>
                <th>Date</th>
                <th>Category</th>
                <th>Description</th>
                <th>Amount</th>
            </tr>
    """

    for exp in expenses:
        html_content += f"""
            <tr>
                <td>{exp['date']}</td>
                <td>{exp['category']}</td>
                <td>{exp['description']}</td>
                <td>₹{exp['amount']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open("expense_report.html", "w") as f:
        f.write(html_content)

    print("HTML report generated as expense_report.html")


# ----------------------------
# Main Menu
# ----------------------------

def main():
    expenses= load_expenses()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Delete Expense")
        print("5. Generate HTML Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summarise_expenses(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            generate_html_report(expenses)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ =="__main__":
    main()

