class Analytics:
    def __init__(self, expenses):
        self.expenses = expenses

    def report(self):
        if not self.expenses:
            print("No data")
            return
        
        total = sum(e.amount for e in self.expenses)
        
        unique_cats = set(e.category for e in self.expenses)
        print(f"Unique Categories (Set): {unique_cats}")

        cat_total = {}
        for e in self.expenses:
            cat_total[e.category] = cat_total.get(e.category, 0) + e.amount
        
        print(f"Category Wise Total (Dict): {cat_total}")
        print(f"Total Spent: {total}")

        try:
            income = float(input("Enter monthly income: "))
            bal = income - total
            if bal >= 0:
                print(f"Saved: {bal}")
            else:
                print(f"Loss: {abs(bal)}")
        except:
            print("Invalid income")