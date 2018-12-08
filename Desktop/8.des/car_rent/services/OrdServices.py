from repositories.OrdRepository import OrdRepository

class OrdService:
    def __init__(self):
        self.__Ord_repo = OrdRepository()

    def add_Ord(self, Ord):
        if self.is_valid_Ord(Ord):
            self.__Ord_repo.add_Ord_csv(Ord)
            
    def is_valid_Ord(self, Ord):
        #here should be some code to 
        #validate the Ord
        #self.__license_plate = license_plate
        #lic_no = Order.get_license_plate_no()
        
        
        return True

    def get_order_no(self):
        return self.__Ord_repo.get_Ord()

    