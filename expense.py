ALLOWED_CATEGORIES = ('food', 'travel', 'shopping', 'bills', 'other')

class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category

    def to_string(self):
        return f"{self.title},{self.amount},{self.category}"

    @staticmethod
    def from_string(line):
        t, a, c = line.strip().split(',')
        return Expense(t, float(a), c)