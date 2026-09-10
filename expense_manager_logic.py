from expense import Expense


class ExpenseManager:
    def __init__(self) -> None:
        self.expenses: list[Expense] = []

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def delete_expense(self, title: str) -> bool:
        for expense in self.expenses:
            if expense.title.lower() == title.lower():
                self.expenses.remove(expense)
                return True
        return False

    def edit_expense(self, title: str, new_expense: Expense) -> bool:
        for i, expense in enumerate(self.expenses):
            if expense.title.lower() == title.lower():
                self.expenses[i] = new_expense
                return True
        return False

    def get_expenses_by_category(self, category: str) -> list[Expense]:
        return [expense for expense in self.expenses if expense.category.lower() == category.lower()]

    def get_total_expenses(self) -> float:
        return sum(expense.amount for expense in self.expenses)

    def show_all_expenses(self) -> None:
        if not self.expenses:
            print("Немає витрат.")
            return
        
        print(f"{'Назва витрати':<20} | {'Дата':<12} | {'Категорія витрат':<15} | uah{'Сума':<10} | {'Додатковий коментар':<30}")

        for expense in self.expenses:
            print(f"{expense.title:<20} | {expense.date:<12} | {expense.category:<15} | uah{expense.amount:<10} | {expense.description:<30}")

