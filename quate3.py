class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнено на {amount} грн. Новий баланс: {self.balance} грн.")
        else:
            print("Сума поповнення повинна бути більшою за 0.")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Недостатньо коштів на рахунку.")
            self.balance -= amount
            print(f"Знято {amount} грн. Залишок: {self.balance} грн.")
        except ValueError as e:
            print("Помилка:", e)

    def check_balance(self):
        print(f"Поточний баланс: {self.balance} грн.")

account = BankAccount("Оксана Іваненко", "UA123456789", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
