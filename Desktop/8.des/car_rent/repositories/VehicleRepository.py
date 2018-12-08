from models.Vehicle import Vehicle
import csv

class VehicleRepository:
    
    def __init__(self):
        self.__Vehicles = []

    
    def add_Vehicle_csv(self, Vehicle):
         with open("./data/vehicle.csv","a+", newline = '', encoding="UTF-8-SIG") as v_file:
             ##Bílnúmer,Framleiðandi,Týpuheiti,Flokkur,Árg.Laus dags,Staðsettur,Skilastaðsetning,Athugasemdir
            license_plate = Vehicle.get_license_plate()
            manufacturer = Vehicle.get_manufacturer()
            subtype = Vehicle.get_subtype()
            vec_class = Vehicle.get_vec_class()
            production_year = Vehicle.get_production_year()
            current_location = Vehicle.get_current_location()
            return_location = Vehicle.get_return_location()
            return_date = Vehicle.get_return_date()
            comments = Vehicle.get_comments()
            csv_writer = csv.writer(v_file,delimiter=";")
            csv_writer.writerow([license_plate,manufacturer,subtype,vec_class,production_year,current_location,return_location,return_date,comments])

            """ def get_Vehicles(self):
            if self.__Vehicles == []:
                with open('./data/vehicle.csv','r',encoding = "ISO-8859-1", newline = '') as veh_file:
                    csv_reader = csv.reader(veh_file,delimiter =";")
                    for line in csv_reader:
                        print(line) """

    def get_Occupied_Vehicles(self):
        counter_i = 0
        if self.__Vehicles == []:
            with open('./data/vehicle.csv','r',encoding = "ISO-8859-1", newline = '') as veh_file:
                csv_reader = csv.reader(veh_file,delimiter =";")
                print("{:<20}{:<30}{:<30}{:<30}".format('Nr.',"Flokkur","Væntanlegir úr leigu","Skilastaðsetning"))
                for line in csv_reader:
                    if line[7] != '0D':
                        print("{:<20}{:<30}{:<30}{:<30}".format(line[0],line[1],line[3],line[5]))
                        counter_i +=1
                print('Fjöldi lausra bíla= {0}. '.format(counter_i))                            

                        
    def get_Available_Vehicles(self):
        counter_i = 0
        if self.__Vehicles == []:
            with open('./data/vehicle.csv','r',encoding = "ISO-8859-1", newline = '') as veh_file:
                csv_reader = csv.reader(veh_file,delimiter =";")
                print("{:<20}{:<30}{:<30}{:<30}".format('Nr.',"Flokkur","Flokkuar","Staðsetning"))
                for line in csv_reader:
                    if line[7] == '0D':
                        print("{:<20}{:<30}{:<30}{:<30}".format(line[0],line[1],line[3],line[5]))
                        counter_i +=1
                print('Fjöldi útleigðra bíla= {0}. '.format(counter_i))    

    def get_Available_Vehicles_by_Class(self,vec_class):
        counter_i = 0
        if self.__Vehicles == []:
            with open('./data/vehicle.csv','r',encoding = "UTF-8-SIG", newline = '') as veh_file:
                csv_reader = csv.reader(veh_file,delimiter =";")
                print("{:<20}{:<30}{:<30}{:<30}".format('Nr.',"Flokkur","Flokkuar","Staðsetning"))
                for line in csv_reader:
                    if (line[7] == '0D' and line[3] ==vec_class): # how do we pass parameter all the way here Daði?
                        print("{:<20}{:<30}{:<30}{:<30}".format(line[0],line[1],line[3],line[5]))
                        counter_i +=1
                print('Fjöldi útleigðra bíla= {0}. '.format(counter_i)) 
                                                
                    


    
       

        return self.__Vehicles

