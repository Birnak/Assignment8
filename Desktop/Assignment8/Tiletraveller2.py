#Birna Karen Arnlaugsdóttir 
#https://github.com/Birnak/Assignment8/blob/master/Desktop/Assignment8/a9tiletrav.py


"""1. Wich implementation was easier and why ? 
        Ég held að fyrsta verkefnið sé auðveldara, finnst auðveldara að nota if lúppur
    
    2. Wich implementation is more radable and why ?
        Finnst fyrsta auðveldara að lesa þar sem ég er með hvern reit inní if lúppu og sé hvað
        gerist ef ég ýti á ákveðinn staf.
    3. Wich problems in the first impementation were you able to solve with later implementation?
        

"""

#Þetta forrit er þannig að þú ert á leiðinni í gegnum völundarhús. Getur farið norður(upp),Austur(hægri),Suður(niður) og vestur(vinstri).
# og ert kanski á punkti 1,1 og ferð norður(upp) þá ferðu á reit 1,2 og svo framvegis. ef þú ferð inn í reit 2,2 eða 2,1 þá geturu bara farið Norður(upp) 
# til þess að komast útúr þessum "lokaða kassa" en þegar þú kemst á endan eða á reit 3,1 þá ertu komin á réttan stað og færð "victory!" sem svar þegar þú
#kemst á leiðarenda.


#Max value á áttum.
EAST_MAX_VALUE = 3
WEST_MAX_VALUE = 1
NORTH_MAX_VALUE = 3
SOUTH_MAX_VALUE = 1


def attir(x,y):
    stadsetning = (x,y)
    if stadsetning == (1,1):
         print("You can travel: (N)orth.")
         ny_stadsetning = kikja_input("nN",stadsetning)
    elif stadsetning == (1,2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        ny_stadsetning = kikja_input("NnEeSs",stadsetning)
    elif stadsetning == (1,3):
        print("You can travel: (E)ast or (S)outh.")
        ny_stadsetning = kikja_input("EeSs",stadsetning)
    elif stadsetning == (2,1):
        print("You can travel: (N)orth.")
        ny_stadsetning = kikja_input("Nn",stadsetning)
    elif stadsetning (2,2):
        print("You can travel: (S)outh or (W)est.")
        ny_stadsetning = kikja_input("SsWw",stadsetning)
    elif stadsetning (2,3):
        print("You can travel: (E)ast or (W)est.")
         ny_stadsetning = kikja_input("EeWw",stadsetning)
    elif stadsetning (3,2):
         print("You can travel: (N)orth or (S)outh.")
         ny_stadsetning = kikja_input("NnSs",stadsetning)
    elif stadsetning (3,3):
        print("You can travel: (S)outh or (W)est.")
        ny_stadsetning = kikja_input("SsWw",stadsetning)
    return ny_stadsetning



def kikja_input(a,stadsetning):
    att = str(input("Direction: "))
    if not kikja_input in a:
        print("Not a valid direction!")
    else:

        y2 = stads[1]
        x2 = stads[0]
        if kikja_input == "N" or kikja_input == "n"
            y2 += 1
        elif kikja_input == "S" or kikja_input == "s"
            y2 -= 1
        elif kikja_input == "E" or kikja_input == "e"
            x2 -= 1
        elif kikja_input == "W" or kikja_input == "w"
            x2 -= 1

    return (y2,x2)

stads = (1,1)
victory = False
x = 1
y = 1

while not victory:
    stads = attir(x,y)
    y = stads[1]
    x = stads[0]
    if x == 3 and y == 1:
        print("Victory!")
        victory = True
