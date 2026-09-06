class Expense:
    def __init__(self, title: str, amount: float, category: str, date: str, description: str) -> None:
        self.title: str = title
        self.amount: float = amount
        self.category: str = category
        self.date: str = date
        self.description: str = description

    def __str__(self):
        return f"{self.title:<20} | {self.date:<12} | {self.category:<15} | uah{self.amount:<10} | {self.description:<30}"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Expense':
        return cls(
            title=data["title"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data["description"]
        )


    