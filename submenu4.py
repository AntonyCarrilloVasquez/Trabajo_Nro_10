import libreria
def super_sayajin():
    print("opcion super sayajin elegida")
    print("")
def fase1():
    print("opcion:fase1 elegida")
    print("")
def poder_300k():
    print("opcion:poder 300k")
    print("")
def submenu_opcion_goku():
    opc=0
    max=4
    while(opc!=max):
        print("### submenu ###")
        print("1. super sayajin ")
        print("2. fase1 ")
        print("3. poder 300k ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            super_sayajin()
        if(opc==2):
            fase1()
        if(opc==3):
            poder_300k()
        #fin_if
    #fin_while

def submenu_opcion_vegeta():
    opc=0
    max=3
    while(opc!=max):
        print("### submenu ###")
        print("1. super sayajin ")
        print("2. fase1 ")
        print("3. poder 300k ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            super_sayajin()
        if(opc==2):
            fase1()
        if(opc==3):
            poder_300k()
        #fin_if
    #fin_while
#fin_def

opc=0
max=3
while(opc!=max):
    print("##### sayajin ####")
    print("1.goku")
    print("2.vegeta")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        submenu_opcion_goku()
    if(opc==2):
        submenu_opcion_vegeta()
    #fin_if
#Fin_while
print("fin del programa")


