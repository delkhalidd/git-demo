class Account:
    _next_account_id = 1
    
    def __init__(self, name, balance):
        self._account_id = Account._next_account_id
        Account._next_account_id += 1
        self.name = name
        self.balance = balance
    
    @property
    def account_id(self):
        return self._account_id
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not (4 <= len(value) <= 15):
            raise RuntimeError("Name should be between 4 and 15 characters.")
        self._name = value
    
    def deposit(self, amount):
        if amount < 0:
            print("Warning: Amount should be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount} successfully. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount < 0:
            print("Warning: Amount should be positive.")
            return
        if self.balance - amount < 0:
            print("Warning: Balance would become negative after withdrawal.")
            return
        self.balance -= amount
        print(f"Withdrawn {amount} successfully. New balance: {self.balance}")
    
    def display_account_details(self):
        print(f"Account ID: {self.account_id}\nName: {self.name}\nBalance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_new_account(self):
        name = input("Enter your name: ")
        balance = float(input("Enter initial balance: "))
        account = Account(name, balance)
        self.accounts[account.account_id] = account
        print(f"Account created successfully. Account ID: {account.account_id}")
    
    def use_existing_account(self):
        account_id = int(input("Enter account ID: "))
        account = self.accounts.get(account_id)
        if not account:
            print("Account not found.")
            return
        while True:
            print("Select an operation:")
            print("1. Get Account Details")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Back To Main Menu")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                account.display_account_details()
            elif choice == 2:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == 4:
                break
            else:
                print("Invalid choice.")
    
    def main_menu(self):
        while True:
            print("Select an option:")
            print("1. Create New Account")
            print("2. Use Existing Account")
            print("3. Quit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.create_new_account()
            elif choice == 2:
                self.use_existing_account()
            elif choice == 3:
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")

bank = Bank()
bank.main_menu()
