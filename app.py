class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid deposit amount. Please enter a positive value.")
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal not allowed.")
            return False
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")
            return False

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nBalance: ${self.balance:.2f}"


# Example Usage:
if __name__ == "__main__":
    # Create a new account
    account1 = BankAccount("John Doe", 1000)

    # Check initial balance
    print(account1)

    # Deposit money
    account1.deposit(500)
    print("After deposit:")
    print(account1)

    # Withdraw money
    account1.withdraw(200)
    print("After withdrawal:")
    print(account1)

    # Attempt to withdraw more than the balance
    account1.withdraw(1500)

    # Check final balance
    print("Final Balance:")
    print(account1)
