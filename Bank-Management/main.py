from bank import Bank
from user import Customer,Admin

Pubali_bank = Bank("Pubali Bank")
admin = Admin("admin","admin@gmail.com","Rajshahi")
Pubali_bank.create_admin(admin)

def user_menu():
    while True:
        currentUser = None

        print("1. Login\n2. Registration\n3. Exit")

        choice = int(input("Enter your option : "))

        if choice == 1:

            account_no = int(input("Enter your Account No : "))
            name = input("Enter your Name : ")
            match = False
            for users in Pubali_bank.account_list:
                if users.account_number == account_no and users.name == name.lower():
                    currentUser = users
                    match = True
                    break
            if match == False:
                print("<--No User Found-->")
            else:
                print("**** Login Successfully ****")


        elif choice == 2:

            name = input("Enter your Name : ")
            email = input("Enter your Email : ")
            address = input("Enter your Address : ")
            print("Account-type:")
            print("1.Savings\n2.Current")
            type = int(input("Choose: "))
            accountType = ""
            if type == 1:
                accountType = "Savings"
            elif type == 2:
                accountType = "Current"
            user = Customer(name,email,address,accountType)
            currentUser = user
            Pubali_bank.create_account(user)
            print(f"--> Registration Successfully -->(Your Account number is : {user.account_number})")


        if currentUser != None:

            while True:
                print(f"Welcome {currentUser.name}")
                print("1. Available Balance")
                print("2. Transaction History")
                print("3. Take a Loan")
                print("4. Deposit")
                print("5. Withdraw")
                print("6. Transfer Amount")
                print("7. Exit")


                choice = int(input("Enter Your Choice : "))


                if choice == 1:
                    user.available_balance()
                elif choice == 2:
                    user.check_transaction_history()
                elif choice == 3:
                    amount = int(input("Enter your request amount : "))
                    user.take_a_loan(Pubali_bank,amount)
                elif choice == 4:
                    amount = int(input("Enter your deposit amount : "))
                    user.deposit(amount)
                elif choice == 5:
                    amount = int(input("Enter your withdraw amount : "))
                    user.withdraw(Pubali_bank,amount)
                elif choice == 6:
                    account_no = int(input("Enter the user account number : "))
                    amount = int(input("Enter your amount : "))
                    user.transfer_amount(Pubali_bank,account_no,amount)
                elif choice == 7:
                    break
                else:
                    print("Invalid!!")

        elif choice == 3:
            break           


def admin_menu():
    while True:

        print("1. Login\n2. Exit")
        current_admin = None
        choice = int(input("Enter your option : "))

        if choice == 1:
            name = input("Enter your Name : ")
            email = input("Enter your Email : ")
            flag = False
            for adm in Pubali_bank.admin_list:
                if name == adm.name and email == adm.email:
                    current_admin = adm
                    flag = True
                    break
            if flag == False:
                print("**** User Not Found ****")
            else:
                print("**** Admin Login Successfully ****")

        elif choice == 2:
            break


        if current_admin != None:
            while True:
                print(f"** Welcome {admin.name} **")
                print("1. Delete User")
                print("2. See all User")
                print("3. Total Bank Balance")
                print("4. Total Bank Loan Balance")
                print("5. On or Off the loan feature")
                print("6. Exit")
                choice = int(input("Enter Your Choice : "))

                if choice == 1:
                    account = int(input("Enter the Account No : "))
                    Pubali_bank.delete_account(account)
                elif choice == 2:
                    Pubali_bank.show_users()
                elif choice == 3:
                    Pubali_bank.check_balance()
                elif choice == 4:
                    Pubali_bank.check_loan()
                elif choice == 5:
                    print(f"1.Turn on Loan\n2. Turn off loan")
                    select = int(input("Select your choice : "))
                    Pubali_bank.loan_feature(select) 
                elif choice == 6:
                    break
                else:
                    print("Invalid!!")


while True:
    print("Welcome!!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        user_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input!!")


