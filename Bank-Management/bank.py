class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.account_list = []
        self.admin_list = []
        self.total_balance = 500000000
        self.total_loan = 0
        self.loan_status = True
        self.is_bankrupt = False

    def create_account(self,account):
        self.account_list.append(account)

    def find_account(self,account_no):
        for account in self.account_list:
            if account.account_number == account_no:
                return account
        return None
    
    def create_admin(self,account):
        self.admin_list.append(account)

    def find_admin_account(self,account_name):
        for acc in self.admin_list:
            if acc.name == account_name:
                return acc
        return None
    
    def delete_account(self,account_no):
        account = self.find_account(account_no)
        if account:
            self.account_list.remove(account)
            print("**** Account deleted Successfully ****")
        else:
            print("Account Not Found!!")

    def show_users(self):
        print("Account_No\tName\tEmail\tAddress\tBalance")
        for user in self.account_list:
            print(f"{user.account_number} {user.name} {user.email} {user.address} {user.balance}")

    def check_balance(self):
        print(f"Total Balance - {self.total_balance}")

    def check_loan(self):
        print(f"Total Loan - {self.total_loan}")
        return self.total_loan

    def loan_feature(self,select):
        if select == 1:
            self.loan_status == True
            print("loan feature is ON Successfully!")
        elif select == 2 :
            self.loan_status == False
            print("Loan feature is OFF Successfully!")
        else:
            print("Invalid!!")
        
