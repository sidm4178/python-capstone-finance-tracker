Personal Finance Tracker 🧾

Project Overview
This is a command-line Python program that helps users track their personal expenses by category. Users can add expenses with descriptions and amounts, view all recorded expenses, and get a summary of total spending by category. The project demonstrates foundational Python skills and is beginner-friendly.

How to Run the Script
2. Save the code in a file named finance_tracker.py
3. Open your terminal
4. Navigate to the folder containing the file:
5. Run the script:
   python finance_tracker.py

Python Concepts Used:
Dictionaries: Used to organize expenses by category. Each category name is a key, and its value is a list of expense entries.

Lists & Tuples: Expenses are stored as tuples (description, amount) within lists under each dictionary key.

Functions: The code is divided into reusable blocks:
  - add_expense() collects and records user input
  - view_expenses() displays individual expenses by category
  - view_summary() calculates and shows total spending per category
  - 
Conditional Statements: Control logic for menu options, input validation, and whether data exists before viewing or summarizing.

Loops:
  - A while loop continuously displays the menu until the user chooses to exit.
  - Nested for loops are used to iterate through dictionary items and expense entries.

Exception Handling:
  - try / except handles invalid numeric input for amounts.
  - raise is used to reject invalid menu numbers and prevent negative expense amounts.

