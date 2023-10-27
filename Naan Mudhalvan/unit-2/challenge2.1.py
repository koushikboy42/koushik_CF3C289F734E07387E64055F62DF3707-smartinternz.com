class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__balance += amount
          print(f"Deposited ${amount}. New balance: ${self.__balance}")
      else:
          print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self, amount):
      if 0 < amount <= self.__balance:
          self.__balance -= amount
          print(f"Withdrew ${amount}. New balance: ${self.__balance}")
      elif amount > self.__balance:
          print("Insufficient funds.")
      else:
          print("Invalid withdrawal amount. Please withdraw a positive amount.")

  def display_balance(self):
      print(f"Account Holder: {self.__account_holder_name}")
      print(f"Account Number: {self.__account_number}")
      print(f"Account Balance: ${self.__balance}")

# Example usage:
account = BankAccount("123456789", "Bhuvan", 1000)
account.display_balance()

account.deposit(500)
account.withdraw(200)
account.display_balance()
