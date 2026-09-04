def view_history():

    try:

        with open("transactions.txt", "r") as file:

            lines = file.readlines()

        return lines
    
    except FileNotFoundError:

        return []

""" 
######### Learning Signature ######### 
Programmed by: Yma Khaliya L. Basio
Date Submitted: September 4, 2026
 
Program Description: This program creates a transaction history module that reads transactions from a file 
and returns the transaction records to the main program.
Reflection: I learned how to read transaction records from a file and handle a missing file by returning an emtpy list.

AI Usage
[ ] No AI Assistance – Completed independently without AI.
[X] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""