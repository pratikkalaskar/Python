class Account:
    
    def __init__(self,bal,acc) -> None:
        self.balance = bal
        self.account_no = acc
        pass

    def debit(self,amount):
        self.balance=self.balance - amount
        print("Rs",amount ,"is debit")
        print("Total amount balance is:",self.print_bal())

    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs",amount, "is credit")
        # print("Rs",amount, "is credit")
        print("Total amount balance is:",self.print_bal())

    def print_bal(self):
        return self.balance

Acc1 = Account(10000,12345)
Acc1.credit(3000)
Acc1.debit(2000)