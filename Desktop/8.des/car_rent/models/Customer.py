class Customer:

    def __init__(self, name, kennitala, phone):
        self.__name = name
        self.__kennitala = kennitala
        self.__phone = phone
    

    def __str__(self):
        return "{},{},{}".format(self.__name, self.__kennitala, self.__phone)
    
    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.__name
    
    def get_kennitala(self):
        return self.__kennitala
    
    def get_phone(self):
        return self.__phone