import libreria
def concierto():
    print("opcion concierto elegida")
    print("")
def cantante():
    print("opcion:cantante elegido")
    print("")
def cantidad_personas_400():
    print("opcion:cantidad de 400 de personas")
    print("")
def submenu_opcion_prince_royce():
    opc=0
    max=4
    while(opc!=max):
        print("### submenu ###")
        print("1. concierto ")
        print("2. cantante ")
        print("3. cantidad de 400 de personas ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            concierto()
        if(opc==2):
            cantante()
        if(opc==3):
            cantidad_personas_400()
        #fin_if
    #fin_while

def submenu_opcion_Bad_bunny():
    opc=0
    max=3
    while(opc!=max):
        print("### submenu ###")
        print("1. concierto ")
        print("2. cantante ")
        print("3. cantidad de 400 de personas ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            concierto()
        if(opc==2):
            cantante()
        if(opc==3):
            cantidad_personas_400()
        #fin_if
    #fin_while
#fin_def

opc=0
max=3
while(opc!=max):
    print("##### cantantes ####")
    print("1.prince royce")
    print("2.bad bunny")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        submenu_opcion_prince_royce()
    if(opc==2):
        submenu_opcion_Bad_bunny()
    #fin_if
#Fin_while
print("fin del programa")


