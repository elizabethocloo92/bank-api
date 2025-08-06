class BankUser:
    def __init__(self, user_name, password, bank):
        #save users user_name
        self.user_name = user_name
        #save users password
        self.__password = password
        #save the bank the user belongs to
        self.bank = bank
        #call create user that will add the user to the bank database
        self.__create_user(bank)
    
    def __create_user(self, bank):
        bank.create_user(self.user_name, self.__password)
          
    
    def check_balance(self):
        
        return self.bank.get_balance(self.user_name , self.__password)
    
    def deposit(self, amount):
        self.bank.deposit(self.user_name, self.password, amount)
        
    def withdraw(self, amount):
        if self.bank['users'][self.iser_name]['balance'] >= amount:
            self.bank['users'][self.user_name]['balance'] -= amount
            return True
        else:
            return False
