
from models.Ord import Ord

import csv

class OrdRepository:
    
    def __init__(self):
        self.__Ord = []   

    def add_Ord_csv(self, Order):
        with open("./data/ord.csv","a+", newline = '', encoding = "UTF-8-SIG") as o_file:  
            
            order_no = Order.get_order_id()
            customer_no = Order.get_customerno()
            
            lic_no = Order.get_license_plate_no()
            start_loc = Order.get_start_location()

            """  self.__order_id = order_dict["ORDER_ID"]
            self.__customerno = order_dict["CUSTOMER_ID"]
            self.__license_plate = order_dict["LICENSE_PLATE_NUMBER"]
            self.__start_location = order_dict["CAR_LOCATION"]
            self.__date_of_order = order_dict["ORDER_DATE"] """
            #ord_d = Ord.get
            #ord_d = Ord.get_or
            #start_date = Ord.get_start
            #return_loc = Ord.get_return_location()
            
            #comments = Ord.get_comments()
            csv_writer = csv.writer(o_file,delimiter=";")

   

            
            #Bílnúmer,Framleiðandi,Týpuheiti,Flokkur,Árg.,Laus,Laus dags,Staðsettur,Skilastaðsetning,Athugasemdir
            #csv_writer.writerow([order_no,customer_no,lic_no,start_loc,return_loc,comments])
            csv_writer.writerow([order_no,customer_no,lic_no,start_loc])

    def get_Ord(self):
        if self.__Ord ==[]:
            with open('./data/ord.csv','r',encoding = "ISO-8859-1", newline = '') as ord_file:
                csv_reader = csv.reader(ord_file,delimiter =";")
                for line in csv_reader:
                    print(line)
        
        return self.__Ord



