
def requested_str(info: str) -> str:
    while True:
        user_input = input(info).strip()
        if user_input:
            return user_input
        else:
            print("Значення не може бути порожнім. Cпробуйте ще раз.")

def requested_float() -> float:
    while True:
        try:
            amount = float(input("Введіть суму витрати: "))
            if amount < 0:
                print("Сума витрати не може бути менше 0. Cпробуйте ще раз.")
            else:
                return amount
        except ValueError:
            print("Введіть цифрове значення.")









def main():

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
                add_expense()
            case 2:
                delete_expense()
            case 3:
                edit_expense()
            case 4:
                show_all_expenses()
            case 5:
                show_expenses_by_category()
            case 6:
                show_total_expenses()
            case 0:
                print("Бувай! Приходь ще!")
                break
            case _:
                print("Будь ласка, введіть дійсний номер дії.")


if __name__ == "__main__":
    main()         