class BankAcount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def __log(self, action):
        print(f"[日志]: {self.owner}执行了{action}操作")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__log("存款")
            print(f"存入{amount}元, 余额{self.__balance}元")
        else:
            print("存款金额必须大于0")

    def withdraw(self, amount):
        if amount <= 0:
            print("取款金额必须大于0")
        elif amount > self.__balance:
             print("余额不足")
        else:
            self.__balance -= amount
            self.__log("取款")
            print(f"取出{amount}元, 余额{self.__balance}元")

    def get_balance(self):
        return self.__balance



account = BankAcount("张三", 1000)
account.deposit(500)
account.withdraw(2000)
account.withdraw(-100)
account.deposit(0)
print(account.get_balance())
