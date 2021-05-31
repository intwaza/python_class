from datetime import datetime, time
class BankAccount:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
        self.loan=0
        self.statement=[]

    def show_balance(self):
        return f"Dear customer {self.name} your balance is {self.balance} ksh"

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"you have deposited"
            }
            self.statement.append(transaction)

            return self.show_balance()

        else:
            return f"Dear customer {self.name} your amount is negative"

      

    def withdraw(self,amount):
        if self.balance <amount:
            return f"Dear customer {self.name}, you don't have enough money to your account"
        else:
            self.balance-=amount
            now = datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"you have withdrawn"
            }
            self.statement.append(transaction)
            return self.show_balance()


    def borrow(self,amount):
        self.loan+=amount
        return f"Dear customer {self.name} you have borrowed {self.loan} ksh"
    def repay(self,amount):
        self.loan-=amount
        return f"Dear customer {self.name} you loan is {self.loan} ksh you have paid {amount}"

    def showStatement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%d/%m/%y")
            print(f"{date}: {Narration} {amount}")
        return 