from models.Customer import Customer

class CustomerRepository:
    
    def __init__(self):
        self.__Customer = []

    def add_Customer(self, Customer):
        with open("./data/customer.txt", "a+", encoding = "UTF-8-SIG") as Customer_file:
            name = Customer.get_name()
            kennitala = Customer.get_kennitala()
            phone = Customer.get_phone()
            Customer_file.write("{},{},{}\n".format(name,kennitala,phone))

    def get_Customer(self):
        #if self.__Customer == []:
        with open("./data/customer.txt", "r",encoding = "UTF-8-SIG") as Customer_file:
            for line in Customer_file.readlines():
                name,kennitala,phone = line.split(",")
                new_Customer = Customer(name,kennitala,phone)
                self.__Customer.append(new_Customer)    
        
        return self.__Customer

