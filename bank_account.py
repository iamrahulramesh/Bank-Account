class Bank_Account:
    def __init__(self):
      self.balance = 0
      print("\nHello,Welcome to your Account")

    def create_username(self,first,last):
        self.first = input("\n Enter your first name: ")
        self.last = input("\n Enter your last name: ")
        self.full =f"{self.first} {self.last}"

        import random
        n = random.randint(0,100)
        username = f"{self.full}.{n}"
        print(f"your username is {username}")



    def deposit(self):
       amount = float(input("Enter the amount: "))
       self.balance += amount
       print("\nThe current balamce is :", amount)

    def withdraw(self):
       amount = float(input("Enter the amount to be taken: "))
       if self.balance>= amount:
                   self.balance -= amount
                   print("\nThe current balancece is :", amount)
       else:
           print("\n Insufficient fund")

    def display(self):
       print("\n the account balance is :", self.balance)

s = Bank_Account()

s.create_username("","")
s.deposit()
s.display()
s.withdraw()
s.display()

