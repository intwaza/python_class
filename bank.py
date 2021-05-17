class BankAccount:
    def __init__(self,accountName,balance):
        self.accountName=accountName
        self.balance=balance
    def Deposit(self,amount):
        return f"Dear customer {self.accountName}, you have deposit {amount} now your balance is {self.balance+amount}"
    def withdraw(self,amount):
        return f"Dear customer {self.accountName}, you have withdraw {amount} now your balance is {self.balance-amount}"

