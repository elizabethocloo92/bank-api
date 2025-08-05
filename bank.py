"""
Important information:
- bank_data will be stored in the following manner

bank_data = {
    "user_name": {
        "password": "users_password",
        "balance": 0.0
    }
}
"""


class Bank:
    def __init__(self, bank_name):
        #set the name of the bank
        self.bank_name = bank_name
        #where all the bank data will be stored
        self.__bank_data = {}

    def __user_login(self, user_name, password):
       if user_name in self.__bank_data:
           if self.__bank_data[user_name]["Password"] == password:
               print("Login Verified")
               return True
           else:
               print("Inccorect Password")
               return False
       else:
           print("User Not in System")
           return False
    def get__bank_data(self):
        return self.__bank_data 
    
    def __process_transaction(self, user_name, amount):
      if user_name in self.__bank_data:
        self.__bank_data[user_name]["balance"] += amount
        return True
      else:
            print("User not found.")
            return False

    def find_user(self, user_name):
       return user_name in self.__bank_data
    
    def create_user(self, user_name, password):
        #check to see if user is not already in the database
        if user_name not in self.__bank_data:
            #add the user to the system
            self.__bank_data[user_name] = {
                "password": password,
                "balance": 0
            }
            print(f"User '(user_name)' created,")
            return True
        else:
            print("User Already in System.")
            return False
            
    def get_balance(self, user_name, password):
        if user_name in self.__bank_data:
            return self.__bank_dta[user_name]["balance"]
        else:
            print("User not in system.")
            return None
        
    
    def deposit(self, user_name, password, amount):
       if amount <=0:
           print("Deposit MUST be greater than 0.")
           return False
           return self.__process_transaction(user_name, amount)

    def withdraw(self, user_name, password, amount):
       if amount <=0:
           print("Withdrawl MUST be greater than 0.")
           return False
           if user_name in self.__bank_data:
            current_balance = self.__bank_data[user_name]["balance"]
            if current_balance >= amount:
                self.__bank_data[user_name]["balance"] -= amount
                return True
            else:
                print("Insufficient Funds.")
       else:
           print("User Not in System.")
           return False
        
