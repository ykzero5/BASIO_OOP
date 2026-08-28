def view_history():
    file = open("transactions.txt", "r")
    lines = file.readlines()
    file.close()

    print("===== TRANSACTION HISTORY =====")

    for line in lines:
        print(line.strip())

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: August 28, 2026
 
Program Description: This program reads the saved ATM transactions from a text file and displays them as transaction history.
Reflection: I learned how to use the readlines(), a for loop, and the strip() to read and display information stored in a text file.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""