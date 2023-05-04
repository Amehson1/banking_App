import random

class Bank:
    def __init__(self):
        self.users = {}

    """Register new User(customer) """
    def register_user(self, Firstname, Lastname, address, phone, email, password):
        user_id = str(random.randint(100000, 9999999))
        user = User(user_id, Firstname, Lastname, address, phone, email, password)
        self.users[user_id] = user
        return user
    
    """ User(customer) login page """
    def login_user(self, email, password):
        for user in self.users.values():
            if user.email == email and user.password == password:
                return user
        return None


class User:
    def __init__(self, user_id, Firstname, Lastname, address, phone, email, password):
        self.user_id = user_id
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        self.accounts = {'Savings': Account('Savings'), 'Current': Account('Current')}
        self.transactions = []

    """Shows updates of the balance or deposit, and credit transaction"""
    def deposit(self, account_type, amount):
        account = self.accounts.get(account_type)
        if account:
            account.deposit(amount)
            self.transactions.append(Transaction('Deposit', amount, account_type))
            print('Deposit successful. New balance:', account.get_balance())
        else:
            print('Invalid account type')

    """Upate all transaction when withdraw and when deposit, and show what is remaining"""
    def transfer(self, from_account_type, to_account_type, amount):
        from_account = self.accounts.get(from_account_type)
        to_account = self.accounts.get(to_account_type)
        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                self.transactions.append(Transaction('Transfer', amount, from_account_type + ' to ' + to_account_type))
                print('Transfer successful. New balance:', from_account.get_balance())
            else:
                print('Insufficient funds')
        else:
            print('Invalid account type')

        """Shows transaction history of a customer """
    def get_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

        """Shows customer balance"""
    def check_balance(self, account_type):
        account = self.accounts.get(account_type)
        if account:
            print('Balance:', account.get_balance())
        else:
            print('Invalid account type')


class Account:
    def __init__(self, account_type):
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        choice.deposit = amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
#     # create an instance of Account
# account = Account("checking")

#     # assign account to choice
# choice = account

#     # call the deposit method on choice and set choice.deposit to amount
# amount = 100
# choice.deposit(amount)
# choice.deposit = amount  # set choice.deposit to amount

# print(choice.balance)  # prints 100
    
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance is {self.balance}.")

#     # create an instance of BankAccount
#     # account = BankAccount()

#     # assign account to choice
#     choice = Account

#     # call the deposit method on choice
#     amount = 100
#     choice.deposit(amount)





class Transaction:
    def __init__(self, transaction_type, amount, account):
        self.transaction_type = transaction_type
        self.amount = amount
        self.account = account

    """Update the trasaction history"""
    def __str__(self):
        return f'{self.transaction_type} of {self.amount} from {self.account}'


# create a new bank instance
bank = Bank()

while True:
    print('Welcome to the bank!')
    print('1. Register')
    print('2. Login')
    print('3. Deposit')
    print('4. View Transaction History')
    print('5. Check balance')
    print('6. Logout')

    choice = input('Enter your choice: ')
    if choice == '1':
        Firstname = input('Enter your first name: ')
        Lastname = input('Enter your last name: ')
        address = input('Enter your address: ')
        phone = input('Enter your phone number: ')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        user = bank.register_user(Firstname, Lastname, address, phone, email, password)
        print('Registration successful. Your user ID is:', user.user_id)
    elif choice == '2':
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        user = bank.login_user(email, password)
        if user:
            print('Login successful. Welcome,', user.name)

    elif choice == '3':
      break
    else:
      print("Invalid choice")
      continue

    while choice:
            print("1. Deposit")
            print("2. Transfer")
            print("3. View transaction history")
            print("4. Check balance")
            print("5. Logout")
            choice = input("Enter choice: ")
            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                choice.deposit(amount)
                print(f"Deposit of {amount} successful")
            elif choice == "2":
                recipient_email = input("Enter recipient email: ")
                amount = float(input("Enter amount: "))
                
                
                # print('1. Deposit')
                # print('2. withdraw')
