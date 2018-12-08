from ui.SalesmanUi import SalesmanUi

def credentials():
    
    username = input("Sláðu inn notendanafn ")
    password = input("Sláðu inn lykilorð ")  
  
    for line in open("./data/access.txt", "r",encoding = "ISO-8859-1").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            print("Innskráning tókst")
            return True
    print("Rangt notendanafn eða lykilorð")
    return False

def main():
    ui = SalesmanUi()
    ui.main_menu()


if credentials():
    main()