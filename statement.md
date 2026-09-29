# Daily Expense Tracker - Statement.md

## Problem Statement
Many people fail to track their small daily expenses, which leads to overspending and lack of savings. There is a need for a simple, offline, modular system to log expenses and view spending habits.

## Project Scope
The project is a CLI-based Daily Expense Tracker built in Python. It uses modular programming with separate files for expense handling, user management, storage, analytics, and validation. The data is handled using Lists and Arrays (Tuple for categories). No complex database or file handling needed for core logic.

## Target Users
- Students for managing pocket money
- Individuals who want to control daily spending
- Anyone who wants to build a savings habit

## High-Level Features (Exactly as per main.py)

1.  **Add Expense (ch == "1"):**
    - Takes Title, Amount, Category as input
    - Validates Amount using `validators.py`
    - Validates Category using `ALLOWED_CATEGORIES` Tuple from `expense.py`
    - Adds expense to storage

2.  **View All Expenses (ch == "2"):**
    - Displays all expenses as: `{i+1}. {e.title} - {e.amount} - {e.category}`

3.  **View Report (ch == "3"):**
    - Uses `Analytics(store.expenses)` from `analytics.py`
    - Calls `analytics.report()` to show monthly/total report

4.  **Show Amounts Array (ch == "4"):**
    - Uses `store.get_amounts_array()` from `storage.py`
    - Prints `Amounts Array: {arr}` for analysis purpose (Array implementation)

5.  **Exit with Thank You Banner (ch == "5"):**
    - Displays "DAILY EXPENSE TRACKER - Thank You!" banner
    - Uses loop `for i in range(1, 6):` to print pattern `₹ * i + | {i*100} Saved!`
    - Shows "Goodbye! Keep Tracking, Keep Saving!"

## Modules Used 
- `expense.py` - Expense class and ALLOWED_CATEGORIES Tuple
- `user_manager.py` - User login
- `storage.py` - Manages list of expenses and get_amounts_array()
- `analytics.py` - Report generation
- `validators.py` - Input validation
- `main.py` - Main menu driver with 5 choices
- `test_basic.py`- Automatically checks if expense tracker code works correctly without bugs

## Technology Stack
- Language: Python
- Concepts Used: List, Tuple, Array, Loop, Functions, if -else-elif control statements, Modular Programming, CLI
