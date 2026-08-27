class BankAcount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"存入{amount}元, 余额{self.balance}元")

    def withdraw(self, amount):
        if amount > self.balance:
             print("余额不足")
        else:
            self.balance -= amount
            print(f"取出{amount}元, 余额{self.balance}元")

    def show_balance(self):
        print(f"户主{self.owner}, 余额{self.balance}元")

account = BankAcount("张三", 1000)
account.deposit(500)
account.withdraw(2000)
account.withdraw(800)
account.show_balance()





      