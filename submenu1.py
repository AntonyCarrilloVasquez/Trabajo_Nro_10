import libreria
def auto_carrera():
    print("opcion auto de carrera elegida")
    print("")
def confg_farosLed():
    print("opcion:faros led elegidos")
    print("")
def velocidad_carro200km():
    print("opcion:velocidad 200km elegida")
    print("")
def submenu_opcion_ferrari():
    opc=0
    max=4
    while(opc!=max):
        print("### autos de carrera ###")
        print("1. auto carrera ")
        print("2. faros led ")
        print("3. velocidad 200 km ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            auto_carrera()
        if(opc==2):
            confg_farosLed()
        if(opc==3):
            velocidad_carro200km()
        #fin_if
    #fin_while

def submenu_opcion_rayomacuin():
    opc=0
    max=3
    while(opc!=max):
        print("### autos de carrera ###")
        print("1. auto carrera ")
        print("2. faros led ")
        print("3. velocidad 200 km ")
        print("4.salir")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            auto_carrera()
        if(opc==2):
            confg_farosLed()
        if(opc==3):
            velocidad_carro200km()
        #fin_if
    #fin_while
#fin_def

opc=0
max=3
while(opc!=max):
    print("##### autos ####")
    print("1.ferrari")
    print("2.rayo macuin")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        submenu_opcion_ferrari()
    if(opc==2):
        submenu_opcion_rayomacuin()
    #fin_if
#Fin_while
print("fin del programa")

