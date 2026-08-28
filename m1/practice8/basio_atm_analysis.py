def analyze_transactions():
    file = open("transactions.txt", "r")
    content = file.read()
    file.close()

    deposit_count = content.count("Deposit")
    first_deposit = content.find("Deposit")

    print("===== TRANSACTION ANALYSIS =====")

    print(f"Total Deposits: {deposit_count}")
    print(f"First Deposit Index: {first_deposit}")

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: August 28, 2026
 
Program Description: This program analyzes the saved ATM transactions by counting the number of deposits and finding the position of the first occurence of "Deposit".
Reflection: I learned how to use count() and find() to analyze information stored in a text file.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""