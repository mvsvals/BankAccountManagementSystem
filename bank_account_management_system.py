# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    # 1. Prompt the user for the account holder's name.
    while True:
        new_account_holder = input('Please input the new account holder\'s name: ').strip()
        if new_account_holder.isspace():
            print('Invalid input!')
            continue
        break
    # 2. Add the new account holder to the list of account holders.
    account_holders.append(new_account_holder)
    # 3. Initialize the balance to 0 for the new account.
    balances.append(0)
    # 4. Initialize an empty transaction history for the new account.
    transaction_histories.append([])
    # 5. Initialize the outstanding loan amount to 0.
    loans.append(0)
    # 6. Notify the user of the successful account creation.
    print('Account created successfully!')


def deposit():
    """Deposit money into an account."""
    # 1. Prompt the user for the account holder's name.
    deposit_account = input('Please input the account holder\'s name for the deposit: ')
    # 2. Check if the account exists in the system.
    if deposit_account in account_holders:
    # 3. If the account exists, prompt the user for the amount to deposit.
        index = account_holders.index(deposit_account)
        deposit_amount = input('Please input the amount you wish to deposit: ')
    # 4. Update the account's balance with the deposited amount.
        balances[index] += float(deposit_amount)
    # 5. Log the transaction in the account's transaction history.
        transaction_histories[index].append(float(deposit_amount))
    # 6. Display the updated balance to the user.
        print(f'The balance for the account is: {balances[index]:.2f}')
    # 7. If the account does not exist, inform the user.
    else:
        print('The account doesn\'t exist.')


def withdraw():
    """Withdraw money from an account."""
    # 1. Prompt the user for the account holder's name.
    withdraw_account = input('Please input the account holder\'s name for the withdrawal: ')
    # 2. Check if the account exists in the system.
    if withdraw_account in account_holders:
    # 3. If the account exists, prompt the user for the amount to withdraw.
        index = account_holders.index(withdraw_account)
        withdraw_amount = input('Please input the amount you wish to withdraw: ')
    # 4. Check if there are sufficient funds for the withdrawal.
        if balances[index] >= float(withdraw_amount):
    # 5. If funds are sufficient, update the balance and log the transaction.
            balances[index] -= float(withdraw_amount)
            transaction_histories[index].append(-float(withdraw_amount))
    # 6. Display the updated balance to the user.
            print(f'The balance for the account is: {balances[index]:.2f}')
    # 7. If insufficient funds, inform the user.
        else:
            print("Insufficient funds!")
    # 8. If the account does not exist, inform the user.
    else:
        print('The account doesn\'t exist.')


def check_balance():
    """Check the balance of an account."""
    # 1. Prompt the user for the account holder's name.
    balance_account = input('Please input the account holder\'s name for the balance check: ')
    # 2. Check if the account exists in the system.
    if balance_account in account_holders:
    # 3. If the account exists, display the current balance.
        index = account_holders.index(balance_account)
        print(f'The balance for the account is: {balances[index]:.2f}')
    # 4. If the account does not exist, inform the user.
    else:
        print('The account doesn\'t exist.')


def list_accounts():
    """List all accounts and their balances."""
    # 1. Check if there are any accounts in the system.
    if account_holders:
    # 2. If there are accounts, loop through each account holder.
        for account in account_holders:
    # 3. Display the account holder's name, balance, and outstanding loan amount.
            index = account_holders.index(account)
            print(f'Account holder: {account}')
            print(f'Balance: {balances[index]:.2f}')
            print(f'Outstanding loan amount: {loans[index]:.2f}\n')

    # 4. If there are no accounts, inform the user.
    else:
        print('There are no existing accounts.')

def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.
    sender_account = input('Please input the sender\'s account name: ')
    recipient_account = input('Please input the recipient\'s account name: ')
    # 2. Check if both accounts exist in the system.
    if sender_account in account_holders and recipient_account in account_holders:
    # 3. If both accounts exist, prompt the user for the amount to transfer.
        sender_index = account_holders.index(sender_account)
        recipient_index = account_holders.index(recipient_account)
        transfer_amount = float(input('Input the amount you wish to transfer: '))
    # 4. Check if the sender has sufficient funds for the transfer.
        if balances[sender_index] >= transfer_amount:
    # 5. If funds are sufficient, update both balances and log the transactions.
            balances[sender_index] -= float(transfer_amount)
            balances[recipient_index] += float(transfer_amount)
            transaction_histories[sender_index].append(-float(transfer_amount))
            transaction_histories[recipient_index].append(float(transfer_amount))
    # 6. Inform the user of the successful transfer.
            print('Transfer successful!')
    # 7. If insufficient funds or if either account does not exist, inform the user.
        else:
            print('Insufficient funds for the transfer.')
    else:
        print(f'The sender account {sender_account} does not exist.') if sender_account not in account_holders else print(f'The recipient account {recipient_account} does not exist.')


def view_transaction_history():
    """View transaction history for a specific account."""
    # 1. Prompt the user for the account holder's name.
    history_account = input('Please input the account name you wish to view the transaction details for: ')
    # 2. Check if the account exists in the system.
    if history_account in account_holders:
    # 3. If the account exists, display the transaction history.
        transaction_index = account_holders.index(history_account)
    # 4. If there are no transactions, inform the user.
        if not transaction_histories[transaction_index]:
            print('There are no transactions for the account.')
        else:
            for transaction in transaction_histories[transaction_index]:
                print(f'* {transaction:.2f}')
    # 5. If the account does not exist, inform the user.
    else:
        print('The account doesn\'t exist.')



def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[index]:
            # Update balance and outstanding loan amount
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")

main()