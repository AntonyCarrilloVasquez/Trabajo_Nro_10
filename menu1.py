import libreria

def AgregarTrabajador():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    cargo=libreria.pedir_ocupacion("ingrese ocupacion:")
    sueldo=libreria.pedir_num("ingrese sueldo:")
    contenido= nombre + "-" + cargo + "-" +str(sueldo) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")

def Leertrabajador():
    print("se agregaron datos")

opc=0
max=3
while(opc!=max):
    #lerr el nombre,cargo,sueldo de un trabajador
    print("### MENU ###")
    print("1.nombre,cargo,sueldo")
    print("2. leer trabajador ")
    print("3. salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if(opc==1):
        AgregarTrabajador()

    if(opc==4):
        Leertrabajador()

