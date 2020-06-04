class Bank_Account:
    def __init__(self):
      self.balance = 0
      print("\nHello,Welcome to your Account")
      self.userid={}

    def create_username(self,first,last):
        self.first = input("\n Enter your first name: ")
        self.last = input("\n Enter your last name: ")
        self.full =f"{self.first} {self.last}"

        import random
        n = random.randint(0,100)
        username = f"{self.full}.{n}"
        print(f"your username is {username}")

        account_no =random.randint(100000,999999)
        print(f"your account number is {account_no}")

    def menu(self):
        print("Select the account type,\n 1.Savings Account \n 2.Salary Account \n 3.Longterm Account")
        choice = input()

        if choice == "1":
            print("Your account is Savings account")

        if choice == "2":
            print("Your account is Salary Account")

        if choice == "3":
            print("Your account is Long term Account")
        
    

    def deposit(self):
          amount = float(input("Enter the amount: "))
          self.balance += amount
          print("\nThe current balamce is :", amount)
    

    def withdraw(self):
       amount = float(input("Enter the amount to be taken: "))
       if self.balance>= amount: 
                   self.balance -= amount
                   print("\nYou withdrew :", amount)
       else:
           print("\n Insufficient fund")

    def display(self):
       print("\n the account balance is :", self.balance)

s = Bank_Account()

s.create_username("","")
s.menu()
s.deposit()
s.display()
s.withdraw()
s.display()

