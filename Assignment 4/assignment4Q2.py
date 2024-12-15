# Simulated user database with username, PIN, and balance
users_db = {
    'user1': {'pin': '1234', 'balance': 5000},
    'user2': {'pin': '5678', 'balance': 10000},
    'user3': {'pin': '91011', 'balance': 3000}
}

# Function to sign in the user
def sign_in():
    username = input("Enter your username: ")
    if username not in users_db:
        print("Username not found. Try again.")
        return None
    pin = input("Enter your PIN: ")
    if pin == users_db[username]['pin']:
        print(f"Welcome {username}!")
        return username
    else:
        print("Incorrect PIN. Try again.")
        return None

# Function to withdraw money
def withdraw(user):
    amount = float(input("Enter amount to withdraw: "))
    if amount > users_db[user]['balance']:
        print("Insufficient funds!")
    else:
        users_db[user]['balance'] -= amount
        print(f"Withdrawal successful! Your new balance is: {users_db[user]['balance']}")

# Function to deposit money
def deposit(user):
    amount = float(input("Enter amount to deposit: "))
    users_db[user]['balance'] += amount
    print(f"Deposit successful! Your new balance is: {users_db[user]['balance']}")

# Function to change PIN
def change_pin(user):
    new_pin = input("Enter new PIN: ")
    confirm_pin = input("Confirm new PIN: ")
    if new_pin == confirm_pin:
        users_db[user]['pin'] = new_pin
        print("PIN changed successfully!")
    else:
        print("PINs do not match. Try again.")

# Main menu of the ATM
def atm_menu(user):
    while True:
        print("\nATM Menu:")
        print("1. Withdraw Amount")
        print("2. Deposit Amount")
        print("3. Change PIN")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            withdraw(user)
        elif choice == '2':
            deposit(user)
        elif choice == '3':
            change_pin(user)
        elif choice == '4':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1-4.")

# Main function to run the ATM Simulator
def main():
    print("Welcome to the ATM Simulator!")
    
    # Sign In Procedure
    user = sign_in()
    if user:
        # If sign-in is successful, show the ATM menu
        atm_menu(user)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
