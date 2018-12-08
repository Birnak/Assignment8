from services.VehicleService import VehicleService 
from models.Vehicle import Vehicle 
from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Ord import Ord

from services.OrdServices import OrdService
from models.System_Maintenance import System_Maintenance


from services.System_MaintenaceServices import System_MaintenanceService

import os # for the cls function
import sys # for status bar
import time # for status bar
import datetime # for clock
now = datetime.datetime.now()
def cls(pm):
    if pm == 'end':
        input('Ýttu á Enter til að að fara aftur í aðalval')  
    os.system('cls' if os.name=='nt' else 'clear')
def update_progress(progress): #breytt og aðlagað, en upprunalega fengið frá:     https://stackoverflow.com/questions/3002085/python-to-print-out-status-bar-and-percentage
    barLength = 40 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Bíðið...\r\n"
    if progress >= 1:
        progress = 1
        status = "Lokið...\r\n"
    block = int(round(barLength*progress))
    text = "\rPrósentum lokið: [{0}] {1}% {2}".format( "="*block + " "*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

class SalesmanUi:
    def __init__(self):
        self.__Vehicle_service = VehicleService()
        self.__Customer_service = CustomerService()
        self.__Ord_service = OrdService()
        self.__System_MaintenanceService = System_MaintenanceService()
        
    def main_menu(self):
        update_progress(-1)    
        time.sleep(.4)
        update_progress(1)    
        time.sleep(.3)
        cls('')
        time.sleep(.2)
        action = ""
        while(action != "h"):
            print("╔════════════════════════════════════════════════════════════════════════════════════╗")
            print("║                                                          ","%d"%now.day + "/" + "%d"% now.month + "/" + "%d"% now.year + " | " + now.strftime( "%H:%M:%S") ,   "    ║")
            print("║--------------------------------------Aðgerðir:-------------------------------------║")
            print("║1. Leigja út bíl (skrá pöntun)                                                      ║")
            print("║2. Skila bíl í lok leigutíma                                                        ║")
            print("║--------------------------------------Skýrslur:-------------------------------------║")
            print("║4. Flétta upp pöntun                                                                ║") 
            print("║6. Birta yfirlit yfir viðskiptamenn                                                 ║")                       
            print("║7. Birta lista yfir lausa bíla                                                      ║")
            print("║8. Birta lista yfir lausa bíla eftir flokkum                                        ║")
            print("║9. Birta lista yfir  bíla í útleigu                                                 ║")
            print("║                                                                                    ║")             
            print("║                                                                                    ║")            
            print("║                                                                                    ║")                                                 
            print("║                                                                                    ║")             
            print("╠════════════════════════════════════════════════════════════════════════════════════╣")
            print("║--------------------------------Uppsetning / viðhald :------------------------------║")
            print("║90. Stofna notanda að kerfinu                                                       ║")            
            print("║91. Stofna viðskiptamann                                                            ║")
            print("║92. Stofna bíl                                                                      ║")
            print("╠════════════════════════════════════════════════════════════════════════════════════╣")
            print("║                                                                                    ║")
            print("║                                                                                    ║")
            print("║Sláðu inn 'h' til að hætta                                                          ║")
            print("╚════════════════════════════════════════════════════════════════════════════════════╝") 
            action = input("Veldu valmöguleika: ").lower()
            if action == "1":
                d = {}
                cls('start') # now, to clear the screen
                d["ORDER_ID"] = input("Sláðu inn pöntunarnúmer: ") 
                d["CUSTOMER_ID"] = input("Nr viðskiptamanns: ")
                d["LICENCE_PLATE_NUMBER"] = input("Bílnúmer: ")
                d["CAR_LOCATION"] = input("Staðsetning bíls í upphafi ")
                d["ORDER_DATE"] = input("Pöntun dags: ")
                
                d["START_DATE"] = input("Start date: ")
                
                """
                ret_loc = input('Skilastaðsetning bíls: ')
                ret_date = input("Skiladags bíls: ")
                pay_meth = input("Greiðslumáti: ")
                card_no  = input("  Kortanúmer (ef við á): ")
                ins_bas = input("Grunntrygging: ")
                ins_xtra = input("Aukatrygging: ")
                com_ = input("Athugasemdir: ") """

                #new_o = Ord(order_n,customer_n,license_plate_n,start_loc,order_d,start_d,ret_loc,ret_date,pay_meth,card_no,ins_bas,ins_xtra,com_)                           
                new_o = Ord(d)                           
                self.__Ord_service.add_Ord(new_o)
                
                


                cls('end')
            elif action == "6":
                cls('')
                customer = self.__Customer_service.get_Customer()
                print(customer)
                cls('end')
            elif action == "7": 
                cls('') # now, to clear the screen
                vehicles = self.__Vehicle_service.get_Available_Vehicles()
                
                #for row in vehicles:
                #   print(row)                 
                cls('end')
            elif action == "8": 
                cls('') # now, to clear the screen
                vec_class = input('Hvaða flokk viltu skoða?  (ath: sýna hér lista yfir mögulega flokka...) ') 
                
                vehicles = self.__Vehicle_service.get_Available_Vehicles_by_Class(vec_class) # does this work?

                cls('end')                
            elif action == "9": 
                cls('') # now, to clear the screen
                vehicles = self.__Vehicle_service.get_Occupied_Vehicles()              
                cls('end')
            elif action == "89":
                cls('')
                newuser = input("Sláðu inn notendanafn: ")
                pwd = input("Sláðu inn lykilorð: ")
                ssn = input("Sláðu inn kennitölu: ")
                name = input('Fullt nafn: ')
                addr = input('Heimilisfang: ')
                phone = input("Símanúmer: ")
                e_mail = input("Tölvupóstfang: ")
                active = 'YES'
                comments = input('Athugasemd: ')
                new_employee = System_Maintenance(newuser,pwd,ssn,name,addr,phone,e_mail,active,comments)
                self.__System_MaintenanceService.add_System_Maintenance(new_employee)              
                cls('end')

#new_veh = Vehicle(license_plate, manuf,subt,v_class, prod_year,curr_loc,return_loc,return_date,com) #0D, simply represents that this car isn't rented out (yet)                
#                self.__Vehicle_service.add_Vehicle(new_veh)

            elif action == "90":
                cls('')
                newuser = input("Sláðu inn notendanafn ")
                pwd = input("Sláðu inn lykilorð ")


                """ file = open("./data/access.txt","a+")
                file.write(newuser)
                file.write(" ")
                file.write(pwd)
                file.write("\n")
                file.close() """
                
                cls('end')
            elif action == "91":
                cls('')
                name = input("Nafn: ")
                kennitala = input("Kennitala: ")
                phone = input("Símanúmer: ")
                new_Customer = Customer(name,kennitala,phone)
                self.__Customer_service.add_Customer(new_Customer)                
                cls('end')
            elif action =='92':
                cls('')
                license_plate = input("Bílnúmer: ")
                manuf = input("Framleiðandi: ")
                subt = input("Undirtegund (týpa) ")
                v_class = input("Flokkur: ")
                prod_year = input("Árgerð: ")
                curr_loc = input("Staðsetning: ")
                return_loc ='' #doesn't apply to cars - until they are rented out
                return_date = '0D'
                com = input("Athugasemdir: ")
                
                #self, license_plate, manufacturer, subtype, vec_class, production_year,current_location,return_location,'',comments
                new_veh = Vehicle(license_plate, manuf,subt,v_class, prod_year,curr_loc,return_loc,return_date,com) #0D, simply represents that this car isn't rented out (yet)                
                self.__Vehicle_service.add_Vehicle(new_veh)
               
                cls('end') 
            elif action =='h':
                time.sleep(.2)
                print('Bíðið - kerfi slekkur á sér og gengur frá')                
                # update_progress() : Displays or updates a console progress bar
                ## Accepts a float between 0 and 1. Any int will be converted to a float.
                ## A value under 0 represents a 'halt'.
                ## A value at 1 or bigger represents 100%
                update_progress(-1)   
                time.sleep(.3)
                update_progress(1)   
                time.sleep(.2)
                print('Sjáumst aftur!') 
                time.sleep(.2)
                cls("")
            else:
                cls('')
                print('Óleyfilegt gildi slegið inn, reyndu aftur.')