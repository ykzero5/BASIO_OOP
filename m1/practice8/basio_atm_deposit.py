def deposit_money(account):
    try:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            success = account.deposit(amount)

            if success:
                file = open("transactions.txt", "a")
                file.write(f"Account: {account.account_name}\n")
                file.write("Transaction: Deposit\n")
                file.write(f"Amount: ₱{amount:.2f}\n")

                print("Deposit successful.")
                print(f"New Balance: ₱{account._balance:.2f}")
                account.check_balance()

        else:
            print("Invalid deposit amount.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: August 28, 2026
 
Program Description: This program allows the user to deposit money into an ATM account, saves successful transactions to a txt file, and displayes the updated balance.
Reflection: I learned how to use an object's method to update its data, validate user input, handle errors, and save transaction information to a file.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""