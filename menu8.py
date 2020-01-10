import libreria
def toyota():
    print("se escogio toyota")
def chevrolet():
    print("se escogio chevrolet")
def honda():
    print("es escogio honda")

opc=0
max=4
while(opc != max):
    print("### MARCAS DE CELULARES")
    print("1. toyota ")
    print("2. chevrolet ")
    print("3. honda ")
    print("4. salir ")

    opc=libreria.pedir_numero("ingrese opcion",1,4)

    if (opc==1):
        toyota()
    if (opc==2):
        chevrolet()
    if (opc==3):
        honda()
