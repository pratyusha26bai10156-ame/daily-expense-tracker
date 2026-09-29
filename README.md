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
- **Concepts Used:** List, Tuple (ALLOWED_CATEGORIES), Array, Loops, Functions, if-else-elif control statements, Modular Programming
- **Modules:** expense.py, user_manager.py, storage.py, analytics.py, validators.py, main.py,test_basic.py
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
### Code Screenshots(8)
### main.py
<img width="1248" height="926" alt="Screenshot (240)" src="https://github.com/user-attachments/assets/e4b61de4-d708-4a32-b374-7f071e336be1" />
<img width="1170" height="790" alt="Screenshot (241)" src="https://github.com/user-attachments/assets/8ff62d1d-a3be-4ea8-b54a-70c5e6834f9c" />
# analytics.py
<img width="1183" height="834" alt="Screenshot (242)" src="https://github.com/user-attachments/assets/21458928-1674-46b5-bf87-f79a59391523" />
# expense.py
<img width="1189" height="734" alt="Screenshot (243)" src="https://github.com/user-attachments/assets/71258721-cbae-4c6f-b9d4-3560ca7e5d50" />
# storage.py
<img width="1155" height="870" alt="Screenshot (244)" src="https://github.com/user-attachments/assets/502a26a9-d07f-4f5a-86cf-afb496d68eab" />
# test_basic.py
<img width="833" height="501" alt="Screenshot (246)" src="https://github.com/user-attachments/assets/d62829a8-66df-444e-ac47-7dd271bca312" />
# user_manager.py
<img width="883" height="555" alt="Screenshot (247)" src="https://github.com/user-attachments/assets/fd896742-f513-4e69-aeb9-aef3d5209a52" />
# validators.py
<img width="887" height="564" alt="Screenshot (248)" src="https://github.com/user-attachments/assets/71133135-3a45-4194-b7d4-de549aac604c" />
### Output Screenshots(2)
# Output 1: Add Expense and View All (Choice 1 ,2)
<img width="1282" height="806" alt="Screenshot (238)" src="https://github.com/user-attachments/assets/a2ea97ae-cc6b-4645-ab98-649cdfe1c672" />
# Output 2: Report, Array and Exit (Choice 3,4,5)
<img width="1216" height="917" alt="Screenshot (239)" src="https://github.com/user-attachments/assets/37f42064-5eb7-48dd-8156-d030362662bb" />

