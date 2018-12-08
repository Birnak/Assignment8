from repositories.VehicleRepository import VehicleRepository

class VehicleService:
    def __init__(self):
        self.__Vehicle_repo = VehicleRepository()

    def add_Vehicle(self, Vehicle):
        if self.is_valid_Vehicle(Vehicle):
            self.__Vehicle_repo.add_Vehicle_csv(Vehicle)
  
    def is_valid_Vehicle(self, Vehicle):
        #here should be some code to 
        #validate the Vehicle
        return True

    #def get_Vehicles(self):                           #unused- delete on monday, if not used by then - hk
    #    return self.__Vehicle_repo.get_Vehicles()     #unused- delete on monday, if not used by then - hk

    def get_Available_Vehicles(self):
        return self.__Vehicle_repo.get_Available_Vehicles()

    def get_Available_Vehicles_by_Class(self,vec_class): 

        return self.__Vehicle_repo.get_Available_Vehicles_by_Class(vec_class)

    def get_Occupied_Vehicles(self):
        return self.__Vehicle_repo.get_Occupied_Vehicles()        

    def get_Vehicles_by_genre(self, genre):
        pass


