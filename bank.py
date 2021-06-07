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
                "Narration":"you have repayed your loan"
            }
            self.statement.append(transaction)

            return f"Dear customer {self.name} you have paid your loan and your new balance is {self.balance}"

    def showStatement(self):
        for transaction in self.statement:
            amount = transaction["amount"]
            Narration= transaction["Narration"]
            time= transaction["time"]
            date= time.strftime("%d/%m/%y")
            print(f"{date}: {Narration} {amount}")
        return 