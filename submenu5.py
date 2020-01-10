import libreria
def angeles():
    print("opcion: angeles elegida")
    print("")
def poder():
    print("opcion:poder elegidos")
    print("")
def bondad_100():
    print("opcion: bondad 100 elegida")
    print("")
def submenu_opcion_gabriel():
    opc=0
    max=4
    while(opc!=max):
        print("### deidades ###")
        print("1. angeles ")
        print("2. poder ")
        print("3. bondad 100 ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            angeles()
        if(opc==2):
            poder()
        if(opc==3):
            bondad_100()
        #fin_if
    #fin_while

def submenu_opcion_judas():
    opc=0
    max=3
    while(opc!=max):
        print("### deidades ###")
        print("1. angeles ")
        print("2. poder ")
        print("3. bondad 100 ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            angeles()
        if(opc==2):
            poder()
        if(opc==3):
            bondad_100()
        #fin_if
    #fin_while
#fin_def

opc=0
max=3
while(opc!=max):
    print("##### supremos ####")
    print("1.gabriel")
    print("2.judas")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        submenu_opcion_gabriel()
    if(opc==2):
        submenu_opcion_judas()
    #fin_if
#Fin_while
print("fin del programa")

