import libreria
def hotelplaya():
    nombre=libreria.pedir_nombre("ingrese hotel(playa,ciudad):")
    cantidad=libreria.pedir_num("ingrese nro de habitaciones de:")
    costo=libreria.pedir_numero("ingrese costo:",100,500)
    contenido= nombre+"-"+str(cantidad)+"-"+str(costo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

def hotelciudad():
    nombre=libreria.pedir_nombre("ingrese hotel(playa,ciudad):")
    cantidad=libreria.pedir_num("ingrese nro de habitaciones de:")
    costo=libreria.pedir_numero("ingrese costo:",100,500)
    contenido= nombre+"-"+str(cantidad)+"-"+str(costo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

opc=0
max=3
while(opc != max):
    print("#### MENU ####")
    print("1. hotel en la playa")
    print("2.hotel en la ciudad")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if(opc==1):
        hotelplaya()
    if(opc==2):
        hotelciudad()
