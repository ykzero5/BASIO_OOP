import streamlit as st

from basio_atm_account import Account
import basio_atm_balance
import basio_atm_deposit
import basio_atm_withdraw
import basio_atm_history
import basio_atm_analysis


if "account" not in st.session_state:
    st.session_state.account = Account(
        "Juan Dela Cruz",
        10000.00
    )

account = st.session_state.account



st.set_page_config(
    page_title="Python ATM",
    page_icon="🏦",
    layout="wide"
)



st.title("PYTHON ATM")

st.write(
    f"Welcome, **{account.account_name}**!"
)

st.divider()


st.sidebar.title("ATM MENU")

choice = st.sidebar.radio(
    "Select an option:",
    [
        "Check Balance",
        "Deposit",
        "Withdraw",
        "View History",
        "Analyze Transactions"
    ]
)
if choice == "Check Balance":

    st.header("Check Balance")

    balance = (
        basio_atm_balance.check_balance(account)
    )

    st.metric(
        "Current Balance",
        f"₱{balance:,.2f}"
    )


elif choice == "Deposit":

    st.header("Deposit Money")

    amount = st.number_input(
        "Enter deposit amount",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Deposit Money"):

        if amount <= 0:

            st.error(
                "Invalid deposit amount."
            )

        else:

            success = (
                basio_atm_deposit.deposit_money(
                    account,
                    amount
                )
            )

            if success:

                st.success(
                    "Deposit successful."
                )

                st.metric(
                    "New Balance",
                    f"₱{account.check_balance():,.2f}"
                )



elif choice == "Withdraw":

    st.header("Withdraw Money")

    st.write(
        f"Available Balance: "
        f"₱{account.check_balance():,.2f}"
    )

    amount = st.number_input(
        "Enter withdrawal amount:",
        min_value=0.0,
        step=100.0,
        format="%.2f"
    )

    if st.button("Withdraw Money"):

        if amount <= 0:

            st.error(
                "Invalid withdrawal amount."
            )

        elif amount > account.check_balance():

            st.error(
                "Insufficient balance."
            )

        else:

            success = (
                basio_atm_withdraw.withdraw_money(
                    account,
                    amount
                )
            )

            if success:

                st.success(
                    "Withdrawal successful."
                )

                st.metric(
                    "New Balance",
                    f"₱{account.check_balance():,.2f}"
                )

elif choice == "View History":

    st.header("Transaction History")

    lines = basio_atm_history.view_history()

    transactions = []
    current_transaction = {}

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("Timestamp:"):
            current_transaction["Timestamp"] = (
                line.replace("Timestamp:", "").strip()
            )

        elif line.startswith("Account:"):
            current_transaction["Account"] = (
                line.replace("Account:", "").strip()
            )

        elif line.startswith("Transaction:"):
            current_transaction["Transaction"] = (
                line.replace("Transaction:", "").strip()
            )

        elif line.startswith("Amount:"):
            current_transaction["Amount"] = (
                line.replace("Amount: ₱", "").strip()
            )

            transactions.append(
                current_transaction.copy()
            )

            current_transaction = {}

    if transactions:

        st.dataframe(
            transactions,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No transactions available."
        )

elif choice == "Analyze Transactions":

    st.header("Transaction Analysis")

    result = (
        basio_atm_analysis.analyze_transactions()
    )


    st.subheader(
        "1. Transaction Summary"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Transactions",
        result["total_transactions"]
    )

    col2.metric(
        "Deposits",
        result["deposits"]
    )

    col3.metric(
        "Withdrawals",
        result["withdrawals"]
    )


    st.divider()

    st.subheader(
        "2. Transaction Amount Analysis"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Deposited",
        f"₱{result['total_deposited']:,.2f}"
    )

    col2.metric(
        "Total Withdrawn",
        f"₱{result['total_withdrawn']:,.2f}"
    )

    col3.metric(
        "Average Transaction",
        f"₱{result['average_transaction']:,.2f}"
    )


    st.divider()

    st.subheader(
        "3. Account Activity Analysis"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Latest Transaction",
        result["latest_transaction"]
    )

    col2.metric(
        "Largest Transaction",
        f"₱{result['largest_transaction']:,.2f}"
    )

    col3.metric(
        "Latest Activity",
        result["latest_timestamp"]
    )

# """ 
# ######### Learning Signature ######### 
# Programmed by: Yma Khaliya L. Basio
# Date Submitted: September 4, 2026
 
# Program Description: This program creates a Streamlit web-based ATM interface that connects the Account object with the balance, deposit, withdrawal,
# history, and analysis modules.
# Reflection: I learned how to connect different Python modules in one Streamlit application and use interface components to perform ATM operations
# and display results.
 
# AI Usage
# [ ] No AI Assistance – Completed independently without AI.
# [ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
# [X] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
# """