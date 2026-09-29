from expense import Expense, ALLOWED_CATEGORIES
from user_manager import UserManager
from storage import Storage
from analytics import Analytics
from validators import validate_amount, validate_category

def main():
    user = UserManager()
    user.login()

    store = Storage()
    store.load()

    print(f"Allowed Categories (Tuple): {ALLOWED_CATEGORIES}")

    while True:
        print("\n1. Add Expense 2. View All 3. View Report 4. Show Array 5. Exit")
        ch = input("Choice: ")

        if ch == "1":
            t = input("Title: ")
            a = input("Amount: ")
            c = input(f"Category {ALLOWED_CATEGORIES}: ")
            if not validate_amount(a):
                print("Invalid amount")
                continue
            if not validate_category(c):
                print("Invalid category")
                continue
            store.add(Expense(t, float(a), c))
            print("Added")

        elif ch == "2":
            for i, e in enumerate(store.expenses):
                print(f"{i+1}. {e.title} - {e.amount} - {e.category}")

        elif ch == "3":
            analytics = Analytics(store.expenses)
            analytics.report()

        elif ch == "4":
            arr = store.get_amounts_array()
            print(f"Amounts Array: {arr}")

        elif ch == "5":
         print("\n" + "="*40)
        print("  DAILY EXPENSE TRACKER - Thank You!")
        print("="*40)
        for i in range(1, 6):
            print("  " + "₹ " * i + f"  | {i*100} Saved!")
        print("="*40)
        print("  Goodbye! Keep Tracking, Keep Saving!")
        print("="*40)
        break

if __name__ == "__main__":
    main()