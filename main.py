import json
import os
from datetime import datetime
from json import JSONDecodeError


class Expense:
    def __init__(self,date,category,description,amount):
        self.date=date
        self.category=category
        self.description=description
        self.amount=amount

    def to_dict(self):
        return{
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount":self.amount
        }
class ExpenseTracker:
    def __init__(self,filename="expense.json"):
        self.filename=filename
        self.expenses=self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            try:
               with open(self.filename,"r",encoding="utf-8")as f:
                  data=json.load(f)
                  return [Expense(**exp)for exp in data]
            except json.JSONDecodeError:
                print("WARNING: Json File is corrupted")
        return []

    def save_expenses(self):
        with open(self.filename,"w",encoding="utf-8")as f:
            json.dump([exp.to_dict() for exp in self.expenses],f,indent=4)

    def add_expense(self,category,description,amount):
        date = input("Enter the date (%d-%m-%y)")
        if not date:
            date=datetime.today().strftime("%d-%m-%Y")
        expense = Expense(date, category, description, amount)
        self.expenses.append(expense)
        self.save_expenses()
    def get_total(self):
        return sum(exp.amount for exp in self.expenses)


#
# # ----------------------------
# # Main Menu
# # ----------------------------

def main():
    tracker= ExpenseTracker()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Total")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, description, amount)
            print("Expense added successfully!")

        elif choice == "2":
            print("Total Expense:", tracker.get_total())

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
