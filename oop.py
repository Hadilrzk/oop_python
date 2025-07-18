class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to {self.owner}'s account. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account. New balance: {self.balance}")
        else:
            print(f"Insufficient funds for {self.owner}. You can only withdraw {self.balance}. Balance remains: {self.balance}")

    def print_account(self):
        print(f"Owner: {self.owner}, Final Balance: {self.balance}")


# Create accounts
account1 = BankAccount("Hadil", 100)
account2 = BankAccount("person", 60)


account1.deposit(50)
account2.deposit(20)

account1.withdraw(100)
account2.withdraw(200)


account1.print_account()
account2.print_account()
