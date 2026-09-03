from datetime import datetime

def withdraw_money(account, amount):
    if amount <= 0:
        return False

    success = account.withdraw(amount)

    if success:
        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with open("transactions.txt", "a") as file:
            file.write(
                f"Timestamp: {timestamp}\n"
            )

            file.write(
                f"Account: {account.account_name}\n"
            )

            file.write(
                "Transaction: Withdraw\n"
            )

            file.write(
                f"Amount: ₱{amount:.2f}\n\n"
            )

        return True

    return False

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: September 4, 2026
 
Program Description: This program creates a withdrawal module that validates the withdrawal amount, withdraws money from an Account object,
and saves successful transactions to a file.
Reflection: I learned how to create a withdrawal function that checks the amount, uses the Account object to withdraw money, 
and records successful withdrawals with a timestamp.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""