from basio_atm_account import Account
import basio_atm_balance
import basio_atm_deposit
import basio_atm_history
import basio_atm_analysis

account = Account("Juan Dela Cruz", 10000)

print("==============================")
print("  PYTHON CLI ATM by BASIO")
print(f"  Welcome, {account.account_name}!")
print("==============================")
 
print()
print("===== ATM MENU by BASIO =====")
print("1. Check Balance")
print("2. Deposit")
print("3. View History")
print("4. Analyze Transactions")
 
choice = input("Choose option: ")

if choice == "1":
    basio_atm_balance.check_balance(account)

elif choice == "2":
    basio_atm_deposit.deposit_money(account)

elif choice == "3":
    basio_atm_history.view_history()

elif choice == "4":
    basio_atm_analysis.analyze_transactions()

else:
    print(f"Invalid option.")

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: August 28, 2026
 
Program Description: This program creates an ATM account object, displays the ATM menu, accepts the user's choice, and allows the user to check the account balance.
Reflection: I learned how to create an object from a class and use the object to access attributes and call methods.
 
AI Usage
[X] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""