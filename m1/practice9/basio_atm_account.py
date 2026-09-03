class Account: 
 
    def __init__(self, name, starting_balance):
        self.account_name = name
        self._balance = starting_balance 
 
    def check_balance(self):
        return self._balance 
 
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True

        else:
            return False 
 
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        
        else:
            return False

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: September 4, 2026
 
Program Description: This program creates an ATM account using a class that stores the account name
and balance and allows checking the balance, depositing money, and withdrawing money.
Reflection: I learned how to create a withdrawal method that checks the withdrawal amount before
changing the account balance.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""