import libreria
def samsung():
    print("se escogio samsung")
def apple():
    print("se escogio apple")
def motorola():
    print("es escogio motorola")

opc=0
max=4
while(opc != max):
    print("### MARCAS DE CELULARES")
    print("1. sammsung ")
    print("2. apple ")
    print("3. motorola ")
    print("4. salir ")

    opc=libreria.pedir_numero("ingrese opcion",1,4)

    if (opc==1):
        samsung()
    if (opc==2):
        apple()
    if (opc==3):
        motorola()
