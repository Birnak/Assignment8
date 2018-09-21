#
#https://github.com/Birnak


#Þetta forrit er þannig að þú ert á leiðinni í gegnum völundarhús. Getur farið norður(upp),Austur(hægri),Suður(niður) og vestur(vinstri).
# og ert kanski á punkti 1,1 og ferð norður(upp) þá ferðu á reit 1,2 og svo framvegis. ef þú ferð inn í reit 2,2 eða 2,1 þá geturu bara farið Norður(upp) 
# til þess að komast útúr þessum "lokaða kassa" en þegar þú kemst á endan eða á reit 3,1 þá ertu komin á réttan stað og færð "victory!" sem svar þegar þú
#kemst á leiðarenda.
import string

rangt_input = False

#Max value á áttum.
EAST_MAX_VALUE = 3
WEST_MAX_VALUE = 1
NORTH_MAX_VALUE = 3
SOUTH_MAX_VALUE = 1

#Hver er verið að fara
notvalid = "Not a valid direction! "
adeins_nordur = "You can only travel: (N)orth."
nordur_austur_sudur = 'You can travel: (N)orth or (E)ast or (S)outh.'
austur_eda_sudur = 'You can travel: (E)ast or (S)outh.'
austur_eda_vestur = 'You can travel: (E)ast or (W)est.'
vestur_eda_sudur = 'You can travel: (S)outh or (W)est.'
nordur_eda_sudur = 'You can travel: (N)orth or (S)outh.'

ny_stadsetning = 0.0

nuverandi_stadsetning = 1.1

while True:

#Ef staðsetningin er á 0.0 þá gerum við :
    if ny_stadsetning != 0.0:
        nuverandi_stadsetning = ny_stadsetning
#Ef staðsetningin er á 1.1 þá gerum við:
    if nuverandi_stadsetning == 1.1:
        if not rangt_input:
            print(adeins_nordur)
        att = str.lower((input("Direction: ")))
        if att != "n":
            print(notvalid)
            rangt_input = True
        else:
            ny_stadsetning = 1.2
            rangt_input = False

#Ef staðsetningin er á 1.2 þá gerum við:
    if nuverandi_stadsetning == 1.2:
        if not rangt_input:
            print(nordur_austur_sudur)
        att = str.lower((input('Direction: ')))

        if att == "n":
            ny_stadsetning = 1.3
            rangt_input = False
        
        elif att == "e":
            ny_stadsetning = 2.2
            rangt_input = False
        
        elif att == "s":
            ny_stadsetning = 1.1
            rangt_input = False
        
        else:
            print(notvalid)
            rangt_input = True
    
    #Ef staðsetningin er 1.3

    if nuverandi_stadsetning == 1.3:
        if not rangt_input:
            print(austur_eda_sudur)
        att= str.lower((input('Direction: ')))


        if att ==  "s":
            ny_stadsetning = 2.3
            rangt_input = False
        
        elif  att == "e":
            ny_stadsetning = 2.3
            rangt_input = False
        
        else:
            print(notvalid)
            rangt_input = True
#Ef staðsetningin er 2.3
        
    if nuverandi_stadsetning == 2.3:
        if not rangt_input:
            print(austur_eda_vestur)
        att= str.lower((input('Direction: ')))

        if att == "w":
            ny_stadsetning = 1.3
            rangt_input = False
        elif att == "e":
            ny_stadsetning = 3.3
            rangt_input = False
        else:
            rangt_input = True
            print(notvalid)


   #ef staðsetningin er  3.3:
    if nuverandi_stadsetning == 3.3:
        print(vestur_eda_sudur)
        att= str.lower((input('Direction: ')))

        if att == "w":
            ny_stadsetning = 2.3
            rangt_input = False
        elif att == "s":
            ny_stadsetning = 3.2
            rangt_input = False
        else:
            rangt_input = True
            print(notvalid)


#Ef staðsetningin er 3.2
    if nuverandi_stadsetning == 3.2:
        if not rangt_input:
            print(nordur_eda_sudur)
        att= str.lower((input('Direction: ')))

        if att == "n":
            ny_stadsetning = 3.3
            rangt_input = False
        elif att == "s":
            ny_stadsetning = 3.1
            rangt_input = False
        else:
            rangt_input = True
            print(notvalid)
    

#Ef staðsetningin er 2.2
    if nuverandi_stadsetning == 2.2:
        if not rangt_input:
            print(vestur_eda_sudur)
        att= str.lower((input('Direction: ')))

        if att == "w":
            ny_stadsetning = 1.2
            rangt_input = False
        elif att == "s":
            ny_stadsetning = 2.1
            rangt_input = False
        else:
            rangt_input = True
            print(notvalid)
    
#Ef staðsetningin er 2.1
    if nuverandi_stadsetning == 2.1:
        if not rangt_input:
            print(adeins_nordur)
        att= str.lower((input('Direction: ')))

        if att == "n":
            ny_stadsetning = 2.2
            rangt_input = False
        else:
            rangt_input = True
            print(notvalid)
    
#Ef staðsetningin er 3.1 þá ertu búin að vinna völundarhúsið.
    if nuverandi_stadsetning == 3.1:
        print("Victory!")

        exit()
