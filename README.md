🏦Bank Account Management System (Python)

A simple Python project demonstrating basic banking operations using Object-Oriented Programming (OOP).


---

📌 Project Overview

This is my first Python mini-project: a Bank Account Management System built using classes and methods.
It performs deposit, withdrawal, and balance check operations in a clean and structured way.


---

✨ Features

Create a bank account with owner name

Deposit money

Withdraw money (with insufficient balance protection)

Check current balance

Clear, simple, OOP-based structure



---

🧠 Concepts Used

Python 3

Object-Oriented Programming (OOP)

Classes & Objects

Constructors (__init__)

Methods

Basic Input/Output



---

📜 Source Code

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

print(acc1.check_balance())
print(acc1.deposit(1500))
print(acc1.withdraw(2000))
print(acc1.withdraw(6000))
print(acc1.check_balance())


---

🖥️ Sample Output

Current balance: ₹5000
Deposited ₹1500. New balance: ₹6500
Withdrew ₹2000. New balance: ₹4500
Insufficient funds!
Current balance: ₹4500


---

👨‍💻 Developer

Developed by: Krishna Maheshwari
First Python Project (Internship Learning)


---

🚀 How to Run

1. Download the project files


2. Run in terminal or VS Code:



python bank_project.py
