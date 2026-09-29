# Daily Expense Tracker

## Project Title
Daily Expense Tracker - CLI Based Personal Finance Manager

## Overview of the Project
This project is a simple, offline CLI-based Daily Expense Tracker developed in Python. It helps users to log daily expenses like Food, Travel, Shopping etc. The system uses modular programming with separate files for each functionality. It stores expenses in a List and also converts them into Array for analysis. It is useful for students and individuals to control spending and build savings habit.

## Features
1.  **Add Expense:** Takes Title, Amount and Category from user. Validates amount and category using validators.
2.  **View All Expenses:** Displays all saved expenses in the format - Title - Amount - Category.
3.  **View Report:** Generates monthly and total expense report using Analytics module.
4.  **Show Amounts Array:** Displays all expense amounts as an Array using get_amounts_array() method.
5.  **Exit:** Shows a Thank You banner with a savings pattern using loop and exits the application.

## Technologies / Tools Used
- **Language:** Python 3
- **Concepts Used:** List, Tuple (ALLOWED_CATEGORIES), Array, Loops, Functions, Modular Programming
- **Modules:** expense.py, user_manager.py, storage.py, analytics.py, validators.py, main.py
- **Tools:** VS Code, Python Terminal, GitHub, Vityarthi Portal

## Steps to Install & Run the Project
1.  Clone or download the project from GitHub.
2.  Open the project folder in VS Code.
3.  Ensure Python is installed by running `python --version` in terminal.
4.  Run the main file: `python main.py`
5.  Login and you will see the menu: 1. Add Expense 2. View All 3. View Report 4. Show Array 5. Exit

## Instructions for Testing
1.  Run `python main.py` and login.
2.  Choose 1 and add Title: Lunch, Amount: 200, Category: Food - It should show "Added".
3.  Choose 1 and enter Amount as abc - It should show "Invalid amount" (Validation testing).
4.  Choose 2 - It should display all expenses you added.
5.  Choose 4 - It should display Amounts Array like [200, 500].
6.  Choose 3 - It should display the expense report.
7.  Choose 5 - It should display Thank You banner and exit.

## Screenshots
