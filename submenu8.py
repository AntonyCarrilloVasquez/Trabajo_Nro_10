import libreria
def pecados():
    print("opcion: pecados elegida")
    print("")
def bondad():
    print("opcion: bondad elegidos")
    print("")
def poder_200():
    print("opcion: poder 200 elegida")
    print("")
def submenu_opcion_King():
    opc=0
    max=4
    while(opc!=max):
        print("### pecados ###")
        print("1. pecados ")
        print("2. bondad ")
        print("3. poder 200 ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            pecados()
        if(opc==2):
            bondad()
        if(opc==3):
            poder_200()
        #fin_if
    #fin_while

def submenu_opcion_Ban():
    opc=0
    max=3
    while(opc!=max):
        print("### pecados ###")
        print("1. pecado ")
        print("2. bondad ")
        print("3. poder 200 ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            pecados()
        if(opc==2):
            bondad()
        if(opc==3):
            poder_200()
        #fin_if
    #fin_while
#fin_def

opc=0
max=3
while(opc!=max):
    print("##### 2 pecados capitales ####")
    print("1.King")
    print("2.Ban")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        submenu_opcion_King()
    if(opc==2):
        submenu_opcion_Ban()
    #fin_if
#Fin_while
print("fin del programa")

