from repositories.CustomerRepository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__Customer_repo = CustomerRepository()

    def add_Customer(self, Customer):
        if self.is_valid_Customer(Customer):
            self.__Customer_repo.add_Customer(Customer)
    
    def is_valid_Customer(self, Customer):
        #here should be some code to 
        #validate the Vehicle
        return True

    def get_Customer(self):
        return self.__Customer_repo.get_Customer()

    