class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(f"{self.name} has {self.balance} in their account")




acc1 = BankAccount("Pritish")
acc2 = BankAccount("Samiksha")
acc1.deposit(500)
acc1.deposit(2)
acc1.withdraw(100)



acc2.deposit(1000)
acc2.deposit(300)
acc2.withdraw(700)



acc1.check_balance()
acc2.check_balance()

