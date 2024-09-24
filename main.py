class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.budgets = []

    def add_budget(self, budget):
        self.budgets.append(budget)


class Budget:
    def __init__(self, budget_id, name, total_amount):
        self.budget_id = budget_id
        self.name = name
        self.total_amount = total_amount
        self.expenses = []
        self.incomes = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_income(self, income):
        self.incomes.append(income)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_remaining_budget(self):
        return self.total_amount - self.get_total_expenses()


class Expense:
    def __init__(self, expense_id, amount, category, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.date = date


class Income:
    def __init__(self, income_id, amount, source, date):
        self.income_id = income_id
        self.amount = amount
        self.source = source
        self.date = date


# Example usage:
user1 = User("1", "John Doe", "john@example.com")
budget1 = Budget("1", "Monthly Budget", 2000)
expense1 = Expense("1", 100, "Food", "2024-09-17")
income1 = Income("1", 500, "Salary", "2024-09-17")

budget1.add_expense(expense1)
budget1.add_income(income1)
user1.add_budget(budget1)

print(user1.__dict__)
