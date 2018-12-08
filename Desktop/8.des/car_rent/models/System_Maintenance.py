class System_Maintenance:

    def __init__(self,uname,passwd,ssn,name,address,phone_no,e_mail,active,comments):        
        self.__uname = uname
        self.__passwd = passwd
        self.__ssn = ssn 
        self.__name = name 
        self.__address = address
        self.__phone_no = phone_no
        self.__e_mail = e_mail
        self.__active = active
        self.__comments = comments

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.__uname,self.__passwd,self.__ssn,self.__name,self.__address,self.__phone_no,self.__e_mail,self.__active,self.__comments)
    
    def __repr__(self):
        return self.__str__()

    def get_uname(self):
        return self.__uname()
    def get_passwd(self):
        return self.__passwd()
    def get_ssn(self):
        return self.__ssn()
    def get_name(self):
        return self.__name()
    def get_address(self):
        return self.__address()
    def get_phone_no(self):
        return self.__phone_no()
    def get_e_mail(self):
        return self.__e_mail()
    def get_active(self):
        return self.__active 
    def get_comments(self):
        return self.__comments()
        