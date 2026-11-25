# Personal Expense Tracker

A simple command-line application for tracking personal income,
expenses, and financial balance, built with Python.

## Features

- Add income and expenses.
- Display the current financial balance.
- View transaction history.
- Validate monetary input.
- Handle invalid input without terminating the application.
- Support monetary values with up to two decimal places.

## Technologies

- Python 3
- Decimal module
- Git
- GitHub

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/VadymMurzin/personal-expense-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd personal-expense-tracker
   ```

3. Run the application:

   ```bash
   python main.py
   ```

No external dependencies are required.

## Project Structure

```text
personal-expense-tracker/
├── main.py
├── README.md
└── .gitignore
```

## Application Functions

| Function | Description |
|---|---|
| `show_menu()` | Displays the application menu |
| `add_income()` | Validates and adds income |
| `add_expense()` | Validates and adds expenses |
| `show_balance()` | Calculates and displays the balance |
| `show_history()` | Displays transaction history |
| `main()` | Controls the application flow |

## Learning Objectives

This project was developed to practice:

- Python fundamentals
- Conditional statements and loops
- Lists and dictionaries
- Functions and parameters
- Local variable scope
- Returning multiple values
- Exception handling
- Input validation
- Decimal arithmetic
- Code refactoring
- Version control with Git and GitHub

## Current Limitations

- Data is stored in memory and is lost when the application closes.
- The application uses a command-line interface.
- The application supports PLN as its currency label.
- The user interface is in Ukrainian.

## Future Improvements

- Persistent data storage
- Transaction categories
- Transaction dates
- Financial reports
- Automated testing

## Author

Vadym Murzin

[GitHub Profile](https://github.com/VadymMurzin)
