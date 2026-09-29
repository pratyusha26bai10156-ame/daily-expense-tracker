from array import array

class Storage:
    def __init__(self, filename="data/expenses.txt"):
        self.filename = filename
        self.expenses = []

    def add(self, exp):
        self.expenses.append(exp)
        self.save()

    def save(self):
        import os
        os.makedirs(os.path.dirname(self.filename),exist_ok=True)
        with open(self.filename, 'w') as f:
            for e in self.expenses:
                f.write(e.to_string()+"\n")

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                from expense import Expense
                for line in f:
                    self.expenses.append(Expense.from_string(line))
        except FileNotFoundError:
            pass

    def get_amounts_array(self):
        arr = array('f', [])
        for e in self.expenses:
            arr.append(e.amount)
        return arr