import libreria
def mandamientos():
    print("opcion mandamientos elegida")
    print("")
def poder():
    print("opcion: poder elegida")
    print("")
def maldad_400():
    print("opcion: maldad 400 elegida")
    print("")
def submenu_opcion_estarossa():
    opc=0
    max=4
    while(opc!=max):
        print("### maldad ###")
        print("1. mandamientos ")
        print("2. poder ")
        print("3. maldad 400 ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            mandamientos()
        if(opc==2):
            poder()
        if(opc==3):
            maldad_400()
        #fin_if
    #fin_while

def submenu_opcion_meliodas():
    opc=0
    max=3
    while(opc!=max):
        print("### maldad ###")
        print("1. mandamientos ")
        print("2. poder ")
        print("3. maldad 400 ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            mandamientos()
        if(opc==2):
            poder()
        if(opc==3):
            maldad_400()
        #fin_if
    #fin_while
#fin_def

opc=0
max=3
while(opc!=max):
    print("##### mandamientos ####")
    print("1. estarossa")
    print("2. meliodas")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        submenu_opcion_estarossa()
    if(opc==2):
        submenu_opcion_meliodas()
    #fin_if
#Fin_while
print("fin del programa")

