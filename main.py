class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"На рахунок {self.account_number} зараховано {amount} грн.")
            else:
                print("Сума повинна бути більшою за 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Сума для зняття повинна бути більшою за 0. ")
        elif amount > self.balance:
            print("Недостатньо коштів на рахунку.")
        else:
            self.balance -= amount
            print(f"З рахунку {self.account_number} було знято {amount} грн.")

    def get_balance(self):
        return self.balance