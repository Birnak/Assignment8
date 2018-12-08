class Ord:
    #def __init__(self, orderno, customerno, license_plate,start_location,order_date,start_date,return_location,return_date,payment_method,card_number,basic_insurance,xtra_insurance,comments):
    def __init__(self, order_dict):
        self.__order_id = order_dict["ORDER_ID"]
        self.__customerno = order_dict["CUSTOMER_ID"]
        self.__license_plate_no = order_dict["LICENCE_PLATE_NUMBER"]
        self.__start_location = order_dict["CAR_LOCATION"]
        self.__date_of_order = order_dict["ORDER_DATE"] 
        self.__start_date = order_dict["START_DATE"]

    def __str__(self):
        #return "{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.__orderno, self.__customerno, self.__license_plate,self.__start_location,self.__order_date,self.__start_date,self.__return_location,self.__return_date,self.__payment_method,self.__card_number,self.__basic_insurance,self.__xtra_insurance,self.__comments)
        return "{},{},{},{},{},{}".format(self.__order_id,self.__customerno, self.__license_plate_no,self.__start_location,self.__date_of_order,self.__start_date)
        
    def __repr__(self):
        return self.__str__()
            

    def get_order_id(self):
        return self.__order_id
    
    def get_customerno(self):
        return self.__customerno
    
    def get_license_plate_no(self):
        return self.__license_plate_no

    def get_start_location(self):
        return self.__start_location

    def get_date_of_order(self):
        return self.__date_of_order

    #def start_date(self):
    #    return self.__start_date
    """
    def get_return_location(self):
        return self.__return_location

    def get_return_date(self):
        return self.__return_date

    def get_payment_method(self):
        return self.__payment_method
    
    def card_number(self):
        return self.__card_number
    
    def basic_insurance(self):
        return self.__basic_insurance

    def xtra_insurance(self):
        return self.__xtra_insurance

    def get_comments(self):
        return self.__comments """

