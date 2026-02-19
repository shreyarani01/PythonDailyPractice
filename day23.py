# Atm Machine
class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
Hello how would you like to proceed?
1. Create pin
2. Deposit
3. Withdraw
4. Check balance
5. Exit
""")
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set successfully!")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount: "))
            self.balance += amount
            print("Deposit successful")
        else:
            print("Invalid pin!")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin!")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print("Balance:", self.balance)
        else:
            print("Invalid pin!")
atm = Atm()
