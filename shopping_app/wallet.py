from ownable import Ownable
class Wallet(Ownable):
    #from ownable import set_owner #nuevo
    def __init__(self, owner):
        self.set_owner(owner)
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount
