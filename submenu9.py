import libreria
def configAuto_android():
    print("opcion: android auto elegida")
    print("")
def confg_farosLed():
    print("opcion:faros led elegidos")
    print("")
def configAutos_potencia500Hp():
    print("opcion: potencia 500HP elegida")
    print("")
def submenu_opcion_confgToyota():
    opc=0
    max=4
    while(opc!=max):
        print("### Config Autos ###")
        print("1. conf android auto ")
        print("2. conf faros led ")
        print("3. potencia de 500 HP ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            configAuto_android()
        if(opc==2):
            confg_farosLed()
        if(opc==3):
            configAutos_potencia500Hp()
        #fin_if
    #fin_while

def submenu_opcion_confgHonda():
    opc=0
    max=3
    while(opc!=max):
        print("### Config Autos ###")
        print("1. conf android auto ")
        print("2. conf faros led ")
        print("3. potencia de 500 HP ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            configAuto_android()
        if(opc==2):
            confg_farosLed()
        if(opc==3):
            configAutos_potencia500Hp()
    #fin_while
#fin_def

opc=0
max=3
while(opc!=max):
    print("##### autos ####")
    print("1.conf toyota")
    print("2.conf honda")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        submenu_opcion_confgToyota()
    if(opc==2):
        submenu_opcion_confgHonda()
    #fin_if
#Fin_while
print("fin del programa")

