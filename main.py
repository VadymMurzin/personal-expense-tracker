from decimal import Decimal, InvalidOperation

def show_menu():
    print("""===== PERSONAL EXPENSE TRACKER =====
    1. Додати дохід
    2. Додати витрату
    3. Переглянути баланс
    4. Історія операцій
    5. Вихід""")

user_income = Decimal("0")
user_costs = Decimal("0")
history_operations = []

def add_income(current_income):
    try:
        income_amount = Decimal(input("Введіть дохід: "))
        if not income_amount.is_finite():
            raise ValueError("Число повинно бути скінченним")
        if income_amount <= 0:
            raise ValueError("Сума повинна бути більшою за нуль")
        if income_amount.as_tuple().exponent < -2:
            raise ValueError("Допускається не більше двох знаків після крапки")
        current_income += income_amount
        return current_income, income_amount
    except (ValueError, InvalidOperation) as e:
        print(f"Помилка: {e}")
        return current_income, None

def add_expense(current_expenses):
    try:
        costs_amount = Decimal(input("Введіть витрати: "))
        if not costs_amount.is_finite():
            raise ValueError("Число повинно бути скінченним")
        if costs_amount <= 0:
            raise ValueError("Сума повинна бути більшою за нуль")
        if costs_amount.as_tuple().exponent < -2:
            raise ValueError("Допускається не більше двох знаків після крапки")
        current_expenses += costs_amount
        return current_expenses, costs_amount
    except (ValueError, InvalidOperation) as e:
        print(f"Помилка: {e}")
        return current_expenses, None

def show_balance(income, expenses):
    balance = income - expenses
    print(f"Баланс: {balance} PLN")

while True:
    show_menu()
    choice = input("\nВиберіть дію: ")
    if choice == "5":
        print("До побачення!")
        break
    elif choice == "1":
        user_income, income_amount = add_income(user_income)
        if income_amount is not None:
            operation_income = {"type": "income", "amount": income_amount}
            history_operations.append(operation_income)
    elif choice == "2":
        user_costs, costs_amount = add_expense(user_costs)
        if costs_amount is not None:
            operation_cost = {"type": "expense", "amount": costs_amount}
            history_operations.append(operation_cost)
    elif choice == "3":
        show_balance(user_income, user_costs)
    elif choice == "4":
        if history_operations:
            for history_operation in history_operations:
                print(f'{history_operation["type"]}: {history_operation["amount"]} PLN')
        else:
            print("Історія операцій порожня")
    else:
        print("Невідома команда. Спробуйте ще раз.")