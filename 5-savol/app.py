class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance 

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            return ("Balans manfiy bo'lishi mumkin emas.")

    @balance.deleter
    def balance(self):
        print("Balans o‘chirildi.")
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so‘m qo‘shildi. Yangi balans: {self.__balance} so‘m.")
        else:
            print("Noto‘g‘ri miqdor.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} so‘m yechildi. Yangi balans: {self.__balance} so‘m.")
        else:
            print("Yetarli mablag‘ mavjud emas yoki noto‘g‘ri miqdor.")

a1 = BankAccount(1000)
a1.deposit(500)       
a1.withdraw(300)     
print(a1.balance)  
a1.balance = 2000     
print(a1.balance)     
