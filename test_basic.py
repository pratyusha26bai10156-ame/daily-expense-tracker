from models.expense import Expense
def test_expense():
    e = Expense("test", 100, "food")
    assert e.amount == 100
    print("Test Passed")

if __name__ == "__main__":
    test_expense()