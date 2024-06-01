from abc import ABC
import random
from transaction_history import Transaction_history


class User(ABC):
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.balance = 0
        self.account_number = random.randint(1,500)
        self.account_type = account_type
        self.loan_limit = 0
        self.transaction_history = []


    def available_balance(self):
        print(f"Your Available Balance is : {self.balance}")


    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            save = Transaction_history("deposit",amount)
            self.transaction_history.append(save)
            print(f"**** {amount} tk deposited successfully ****")
        else:
            print("Your Amount is less than 0")



    def withdraw(self,bank,amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        elif amount < 0:
            print("Your Withdrawal amount is less than 0")
        elif bank.is_bankrupt == True:
            print("** the bank is bankrupt -->")
        else:
            self.balance -= amount
            save = Transaction_history("withdraw",amount)
            self.transaction_history.append(save)
            print(f"**** Withdraw {amount}  tk processed Successfully ****")



    def take_a_loan(self,bank,amount):
        
        if self.loan_limit <= 2:
            if amount < 0:
                print("your request amount is less than 0")
            elif amount > bank.total_balance:
                print("Your request amount is out of bound of bank total balance")
            elif bank.loan_status == False:
                print("You can't take loan from bank")
            else:
                self.balance += amount
                save = Transaction_history("loan",amount)
                self.transaction_history.append(save)
                self.loan_limit += 1
                bank.total_balance -= amount
                bank.total_loan += amount
                print("**** loan has been taken Successfully ****")
        else:
            print("Your Loan Limit Exceeded")


    def check_transaction_history(self):
        print("*****Transaction History*****")
        print("**** Details\tAmount ****")
        for transaction in self.transaction_history:
            print(f"**** {transaction.type} {transaction.amount}")


    def transfer_amount(self,bank,account_no,amount):
        search = bank.find_account(account_no)
        if search:
            if amount < 0:
                print("your request amount is less than 0")
            elif amount > self.balance:
                print("Your amount is out of your balance")
            elif bank.is_bankrupt == True:   
                print("the bank is bankrupt!!")
            else:
                print("search-->")
                print(search.balance)
                search.balance += amount
                self.balance -= amount
                save = Transaction_history("transfer money",amount)
                self.transaction_history.append(save)
                print(f"**** {amount} tk has been transferred successfully ****")
        else:
            print("Account does not exist!!")



class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

