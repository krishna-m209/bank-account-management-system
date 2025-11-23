class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount}. New balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew ₹{amount}. New balance: ₹{self.balance}"

    def check_balance(self):
        return f"Current balance: ₹{self.balance}"


# --- Using the BankAccount class ---
acc1 = BankAccount("Karan", 5000)

print(acc1.check_balance())   # Check initial balance
print(acc1.deposit(1500))     # Deposit money
print(acc1.withdraw(2000))    # Withdraw money
print(acc1.withdraw(6000))    # Try to withdraw too much
print(acc1.check_balance())   # Final balance
