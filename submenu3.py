import libreria
def aviones():
    print("opcion:aviones elegida")
    print("")
def alas():
    print("opcion: alas elegidas")
    print("")
def velocidad_avion400km():
    print("opcion:velocidad 400km elegida")
    print("")
def submenu_opcion_XRL():
    opc=0
    max=4
    while(opc!=max):
        print("### sub menu ###")
        print("1. aviones ")
        print("2. alas ")
        print("3. velocidad 400 km ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            aviones()
        if(opc==2):
            alas()
        if(opc==3):
            velocidad_avion400km()
        #fin_if
    #fin_while

def submenu_opcion_trueno():
    opc=0
    max=3
    while(opc!=max):
        print("### submenu ###")
        print("1. aviones ")
        print("2. alas ")
        print("3. velocidad 400 km ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            aviones()
        if(opc==2):
            alas()
        if(opc==3):
            velocidad_avion400km()
        #fin_if
    #fin_while
#fin_def

opc=0
max=3
while(opc!=max):
    print("##### aviones ####")
    print("1.XRL")
    print("2.trueno")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        submenu_opcion_XRL()
    if(opc==2):
        submenu_opcion_trueno()
    #fin_if
#Fin_while
print("fin del programa")

