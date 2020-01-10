import libreria
def informacion():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    apellido=libreria.pedir_apellido("ingrese apellido:")
    vivienda=libreria.pedir_ocupacion("ingrese vivienda:")
    contenido= nombre + "-" + apellido +"-"+ vivienda +"/n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")

def leerinformacion():

    print("se agregaron los datos")

opc=0
max=3
while(opc!=max):
    #leer el nombre,apellido y vivienda de una persona:
    print("## MENU##")
    print("1. nombre,apellido,vivienda")
    print("2. leer informacion")
    print("3. salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if(opc==1):
        informacion()
    if(opc==4):
        leerinformacion()
