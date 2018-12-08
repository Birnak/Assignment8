from models.System_Maintenance import System_Maintenance
import csv
class System_MaintenanceRepository:
    def __init__(self):
        self.__System_Maintenance = []

    
    def add_System_Maintenance_csv(self, System_Maintenance):
         with open("./data/access.csv","a+", newline = '', encoding = "UTF-8-SIG") as v_file:
            
            uname = System_Maintenance.uname()
            passwd = System_Maintenance.passwd()
            ssn = System_Maintenance.ssn()
            name = System_Maintenance.name()
            address = System_Maintenance.address()
            phone_no = System_Maintenance.phone_no()
            e_mail = System_Maintenance.e_mail()
            active = System_Maintenance.active()     
            comments = System_Maintenance.comments()



            csv_writer = csv.writer(v_file,delimiter=";")
            csv_writer.writerow([uname,passwd,ssn,name,address,phone_no,e_mail,active,comments])

    def get_availablesystem_maintenance(self):
        pass
        """ if self.__System_Maintenances == []:
            with open('./data/access.csv','r',encoding = "ISO-8859-1", newline = '') as x_file:
                csv_reader = csv.reader(x_file,delimiter =";")
                for line in csv_reader
                    print(line)
 """
       

        return self.__System_Maintenance

