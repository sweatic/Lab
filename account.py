class Account:
    def __init__(self, name:str) -> None:
        '''
        Function sets up instance of an object
        :param name: Account name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount:float) -> bool:
        '''
        Method to deposit funds
        :param amount: Amount deposited
        :return: True if successful, False if unsuccessful
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True
    def withdrawl(self, amount:float) -> bool:
        '''
        Method to withdrawl funds
        :param amount: Amount to withdrawl
        :return: True if successful, False if unsuccessful
        '''
        if amount > self.__account_balance or amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        Method gets balance
        :return: current balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method returns name of account
        :return: returns account name
        '''
        return self.__account_name

