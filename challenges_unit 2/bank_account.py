class bank_account:
    def __init_(self):
        self.balance=0
        print("hello!!!welcome to the deposit & withdrawl machine")
    def __deposit(self):
        amount=float(input("enter amount to be deposited:"))
        self.balance += amount
        print("\n amount deposited:",amount)
    def __withdraw(self):
        amount=float(input("enter amount to be withdraw:"))
        if self>balance>=amount:
           self.balance-=amount
           print("\n you withdraw:",amount)
        else:
            print("\n Insufficiant balance")
    def display(self):
        print("\n net available balance=",self.balance)
s=bank_account()
s.deposit()
s.withdraw()
s.display()
         
