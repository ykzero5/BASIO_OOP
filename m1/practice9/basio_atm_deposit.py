from datetime import datetime

def deposit_money(account, amount):
    if amount <= 0:
        return False

    success = account.deposit(amount)

    if success:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("transactions.txt", "a") as file:

            file.write(f"Timestamp: {timestamp}\n")

            file.write(f"Account: {account.account_name}\n")

            file.write("Transaction: Deposit\n")

            file.write(f"Amount: ₱{amount:.2f}\n\n")
        return True
    
    return False

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: September 4, 2026
 
Program Description: This program creates a deposit module that validates the deposit amount, deposits money into an Account object,
and saves the transaction information to a file.
Reflection: I learned how to create a deposit function that works with an Account object and saves successful transactions 
with a timestamp.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""