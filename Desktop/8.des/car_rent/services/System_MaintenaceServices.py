
from repositories.SystemMaintenanceRepository import System_MaintenanceRepository

class System_MaintenanceService:
    def __init__(self):
        self.__System_Maintenance_repo = System_MaintenanceRepository()

    def add_System_Maintenance(self, System_Maintenance):
        if self.is_valid_System_Maintenance(System_Maintenance):
            self.__System_Maintenance_repo.add_System_Maintenance_csv(System_Maintenance)
  
    def is_valid_System_Maintenance(self, System_Maintenance):
        #here should be some code to 
        #validate the System_Maintenance
        return True

    def get_Available_System_Maintenance(self):
        return self.__System_Maintenance_repo.get_availablesystem_maintenance()
      

       
        


            