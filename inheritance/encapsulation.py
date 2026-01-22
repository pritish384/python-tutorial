class Account:
    def __init__(self):
        self.__balance = 0   # private

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance

a = Account()
a.deposit(1000)
print(a.get_balance())
