class Account:

    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance

    def check_balance(self):
        print(f"Current Balance: ₱{self._balance:.2f}")

    def deposit(self, amount):
 
        if amount > 0:
            self._balance = self._balance + amount
            return True
 
        else:
            return False

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: August 28, 2026
 
Program Description: This program creates an ATM account using a class that will store the account name and balance and allows the user to check the balance and make a deposit.
Reflection: I learned how to use a class, attributes and methods to organize related data and functions in one object.
 
AI Usage
[X] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""