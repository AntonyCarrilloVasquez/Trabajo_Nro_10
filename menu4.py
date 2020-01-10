import libreria
def stanford():
    print("se escogio stanford")
def loro():
    print("se escogio loro")
def justus():
    print("es escogio justus")

opc=0
max=4
while(opc != max):
    print("### MARCAS DE CELULARES")
    print("1. stanford ")
    print("2. loro ")
    print("3. justus ")
    print("4. salir ")

    opc=libreria.pedir_numero("ingrese opcion",1,4)

    if (opc==1):
        stanford()
    if (opc==2):
        loro()
    if (opc==3):
        justus()
