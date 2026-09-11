from expense import Expense
from expense_manager_logic import ExpenseManager

def requested_str(info: str) -> str:
    while True:
        user_input = input(info).strip()
        if user_input:
            return user_input
        else:
            print("Значення не може бути порожнім. Cпробуйте ще раз.")

def requested_description(info: str) -> str:
    return input(info).strip()  # Description can be empty, so no validation needed

def requested_float(info: str) -> float:
    while True:
        try:
            amount = float(input("Введіть суму витрати: "))
            if amount < 0:
                print("Сума витрати не може бути менше 0. Cпробуйте ще раз.")
            else:
                return amount
        except ValueError:
            print("Введіть цифрове значення.")

def add_expense(expense_manager: ExpenseManager) -> None:
    title = requested_str("Введіть назву витрати: ")
    amount = requested_float("Введіть суму витрати: ")
    category = requested_str("Введіть категорію витрати: ")
    date = requested_str("Введіть дату витрати (у форматі РРРР-ММ-ДД): ")
    description = requested_description("Введіть додатковий коментар до витрати: ")

    expense = Expense(title, amount, category, date, description)
    expense_manager.add_expense(expense)
    expense_manager.save_expenses()
    print(f"Витрата '{title}' додана.")

def delete_expense(expense_manager: ExpenseManager) -> None:
    title = requested_str("Введіть назву витрати, яку хочете видалити: ")
    if expense_manager.delete_expense(title):
        expense_manager.save_expenses()
        print(f"Витрата видалена.")
    else:
        print(f"Витрата '{title}' не знайдена.")

def edit_expense(expense_manager: ExpenseManager) -> None:
    title = requested_str("Введіть назву витрати, яку хочете редагувати: ")
    for expense in expense_manager.expenses:
        if expense.title.lower() == title.lower():
            print(f"Редагування витрати '{title}':")
            new_title = requested_str("Введіть нову назву витрати: ")
            new_amount = requested_float("Введіть нову суму витрати: ")
            new_category = requested_str("Введіть нову категорію витрати: ")
            new_date = requested_str("Введіть нову дату витрати (у форматі РРРР-ММ-ДД): ")
            new_description = requested_description("Введіть новий додатковий коментар до витрати: ")

            new_expense = Expense(new_title, new_amount, new_category, new_date, new_description)
            expense_manager.edit_expense(title, new_expense)
            expense_manager.save_expenses()
            print(f"Витрата '{title}' відредагована.")
            return
    print(f"Витрата '{title}' не знайдена.")


def main() -> None:
    expense_manager = ExpenseManager()
    expense_manager.load_expenses()

    while True:
        print("\n====== Expense Manager MENU ======")
        print("1 -> Додати витрату")
        print("2 -> Видалити витрату")
        print("3 -> Редагувати витрату")
        print("4 -> Показати всі витрати")
        print("5 -> Показати витрати за категорією")
        print("6 -> Показати загальну суму витрат")
        print("0 -> Вийти з програми")

        try:
            user_choice = int(input("\n Введіть номер дії: "))
        except ValueError:
            print("Будь ласка, введіть дійсний номер дії.")
            continue

        match user_choice:
            case 1:
                add_expense(expense_manager)
            case 2:
                delete_expense(expense_manager)
            case 3:
                edit_expense(expense_manager)
            case 4:
                expense_manager.show_all_expenses()
            case 5:
                category = requested_str("Введіть категорію витрат: ")
                expenses = expense_manager.get_expenses_by_category(category)
                if expenses:
                    print(f"\nВитрати за '{category}':")
                    print(f"{'Назва витрати':<20} | {'Дата':<12} | {'Категорія витрат':<15} | uah{'Сума':<10} | {'Додатковий коментар':<30}")
                    for expense in expenses:
                        print(expense)
                else:
                    print(f"Витрат за '{category}' не знайдено.")
            case 6:
                total = expense_manager.get_total_expenses()
                print(f"\nЗагальна сума витрат: uah{total:.2f}")
            case 0:
                print("Бувай! Приходь ще!")
                break
            case _:
                print("Будь ласка, введіть дійсний номер дії.")


if __name__ == "__main__":
    main()   
