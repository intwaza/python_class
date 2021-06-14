from datetime import datetime
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
        try:
            10+amount
        except TypeError:
            return f"Dear customer {self.name} the amount must be figures"
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
        try:
            10+amount
        except TypeError:
            return f"Dear customer {self.name} the amount must be figures"
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
        try:
            10+amount
        except TypeError:
            return f"Dear customer {self.name} the amount must be figures"
        limit=10/100
        if amount<0:
            return "sorry we can't give you this loan it is too loan"
        elif self.loan>0:
            return f"Dear customer you still have a loan of {self.loan}"
        elif amount>=self.balance*limit:
            return f"Dear customer you can't borrow that money is lower than a limit of {self.balance*limit}"
        else:
            loan=amount*1.05
            self.balance+=amount
            self.loan=loan

            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"you have borrowed"
            }
            self.statement.append(transaction)

            return f"Dear customer {self.name} you have borrowed {self.loan} ksh"

    def repay(self,amount):
        try:
            10+amount
        except TypeError:
            return f"Dear customer {self.name} the amount must be figures"
        if amount<0:
            return "Dear customer your payment is too low"
        elif amount<=self.loan:
            self.loan-=amount
            return f"Dear customer you have fully paid your loan"
        else:
            payment=amount-self.loan
            self.loan=0
            self.balance+=payment

            now= datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"you have repaid your loan"
            }
            self.statement.append(transaction)

            return f"Dear customer {self.name} you have paid your loan and your new balance is {self.balance}"
    
    def transfer(self,account,amount):
        try:
            10+amount
        except TypeError:
            return f"Dear customer {self.name} the amount must be figures"
        fee= amount*0.05
        Total=fee+amount
        if amount<0:
            return f"Dear customer {self.name} your amount is too low"
        elif Total>self.balance:
            return f"Dear customer {self.name} you balance is {self.balance} and you need atleast {Total}"
        else:
            self.balance-=Total
            account.deposit(amount)
            return f"Dear customer you  have sent {amount} to {account.name}"

    def showStatement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%d/%m/%y")
            print(f"{date}: {Narration} {amount}")
        return 

class MobileMoneyAccount(BankAccount):
    def __init__(self, name, phone_number,service_provider):
        BankAccount.__init__(name, phone_number)
        self.service_provider= service_provider
    
    def buy_airtime(self,amount):
        try:
            10+amount
        except TypeError:
            return f"Dear customer {self.name} the amount must be figures"
        if amount<0:
            return f"Dear customer {self.name} you amount {amount} is too low"
        elif self.balance<amount:
            return f"Dear customer your balance is {self.balance} is too low you can't buy airtime"
        else:
            self.balance-=amount
            return f"Dear customer you have bought airtime of {amount}, your new balance is {self.balance}"