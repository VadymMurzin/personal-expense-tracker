from decimal import Decimal, InvalidOperation

user_income = Decimal("0")
user_costs = Decimal("0")
history_operations = []


while True:
    print("""===== PERSONAL EXPENSE TRACKER =====
1. Додати дохід
2. Додати витрату
3. Переглянути баланс
4. Історія операцій
5. Вихід""")
    choice = input("\nВиберіть дію: ")
    if choice == "5":
        print("До побачення!")
        break
    elif choice == "1":
        try:
            income_amount = Decimal(input("Введіть дохід: "))
            if not income_amount.is_finite():
                raise ValueError("Число повинно бути скінченним")
            if income_amount <= 0:
                raise ValueError("Сума повинна бути більшою за нуль")
            if income_amount.as_tuple().exponent < -2:
                raise ValueError("Допускається не більше двох знаків після крапки")
            user_income += income_amount
            operation_income = {"type": "income", "amount": income_amount}
            history_operations.append(operation_income)
        except (ValueError, InvalidOperation) as e:
            print(f"Помилка: {e}")
    elif choice == "2":
        try:
            costs_amount = Decimal(input("Введіть витрати: "))
            if not costs_amount.is_finite():
                raise ValueError("Число повинно бути скінченним")
            if costs_amount <= 0:
                raise ValueError("Сума повинна бути більшою за нуль")
            if costs_amount.as_tuple().exponent < -2:
                raise ValueError("Допускається не більше двох знаків після крапки")
            user_costs += costs_amount
            operation_cost = {"type": "expense", "amount": costs_amount}
            history_operations.append(operation_cost)
        except (ValueError, InvalidOperation) as e:
            print(f"Помилка: {e}")
    elif choice == "3":
        balance = user_income - user_costs
        print(balance)
    elif choice == "4":
        if history_operations:
            for history_operation in history_operations:
                print(f'{history_operation["type"]}: {history_operation["amount"]} PLN')
        else:
            print("Історія операцій порожня")
    else:
        print("Невідома команда. Спробуйте ще раз.")