# 🔒 Private members in Python
# Use __prefix to mark members as private (e.g., __balance)
# Access restricted within the class only (via name mangling)
# Helps hide sensitive data or internal logic




# 📘 BankAccount Scenario             | 🔒 Private Attributes:
# Class: BankAccount                 | - __account_number: unique ID
#                                    | - __account_holder: account holder's name
#                                    | - __balance: current balance

# 🛠️ Methods:                        | 💡 Notes:
# - __init__(...): set initial data  | - All attributes are private
# - deposit(amount): add balance     | - No direct access from outside
# - withdraw(amount): check & deduct | - Methods handle all operations
# - display_balance(): show balance  | - No getters/setters used

from datetime import datetime
import random

class BankAccount:
    
    # Private class-level attribute for account number counter
    
    def __init__(self, account_holder, balance, Id):
        # Private instance attributes (can't be accessed outside)
        self.__account_number = BankAccount.__generate_account_number()
        self.__account_holder = account_holder
        self.__balance = balance
        self.__Id = Id
        self.__role = "Customer"  # Default role is Customer
    
    # Private method to generate a unique account number (for each account)
    @staticmethod
    def __generate_account_number():
        # Generate a random number between 100000 and 999999 (6-digit number)
        return random.randint(100000, 999999)

    # Public method to display balance (accessible to authorized roles only)
    def display_balance(self, staff):
        if staff.role in ["Staff", "Officer", "Manager"]:  # Check if staff has access
            print(f"Account Number: {self.__account_number}")  # Display private account number
            print(f"Account Holder: {self.__account_holder}")  # Display private account holder name
            if self.__balance == 0:  # Check if balance is zero
                print("⚠️ Your account balance is now 0.00.")
                print("Please deposit funds to avoid future transaction issues.")
            else:
                print(f"Bank Balance: {self.__balance}")  # Display private balance
        else:
            print("Confidential Information. Not accessible for you.")  # Unauthorized access message
        print("-------------------------------")

    # Public method to deposit money into the account
    def deposit(self, amount):
        self.__balance += amount  # Add deposited amount to balance
        timestamp = datetime.now().strftime("%B %d, %Y - %I:%M %p")  # Get current timestamp
        print(f"""💳 Deposit Successful!
🧑‍💼 Account Holder: {self.__account_holder}
💸 Amount deposited: {amount}
💼 New balance: {self.__balance}
🕒 Date/Time: {timestamp}
Thank you for banking with us.""")

    # Private method to check if the provided ID matches the account ID
    def __check_id(self, Id):
        return self.__Id == Id  # Return True if IDs match, else False

    # Public method to withdraw money from the account
    def withdraw(self, amount, Id):
        if self.__check_id(Id):  # Ensure ID matches before proceeding
            print("Checking balance...")  # Inform user that balance is being checked
            if amount > self.__balance:  # Check if withdrawal amount exceeds balance
                print("❌ Insufficient Balance ❌")  # Insufficient funds message
                return
            else:
                self.__balance -= amount  # Deduct withdrawal amount from balance
                timestamp = datetime.now().strftime("%B %d, %Y - %I:%M %p")  # Get current timestamp
                print(f"""✅ Withdrawal successful.
💸 Amount withdrawn: {amount}
💼 Remaining balance: {self.__balance}
🕒 Date/Time: {timestamp}
Thank you for banking with us.""")  # Show withdrawal transaction details
        else:
            print("🚨 Unauthorized ID detected!")  # Intruder alert for incorrect ID

# Staff class to simulate role-based access
class Staff:
    def __init__(self, name, role, employee_id):
        self.name = name
        self.role = role
        self.employee_id = employee_id

# Creating test accounts and staff
test_account1 = BankAccount("Anirban Paul", 10000, "ID2025")
test_account2 = BankAccount("APL", 50000, "ID2225")
staff = Staff("ABC", "Officer", "EC456")

# Displaying balance (only accessible by roles with permission)
test_account1.display_balance(staff)
test_account2.display_balance(staff)

# Depositing money into account
test_account1.deposit(5000)

# Display updated balance after deposit
test_account1.display_balance(staff)

# Withdrawing money from account
test_account2.withdraw(12000, "ID2225")

# Display balance after withdrawal
test_account2.display_balance(staff)

