import libreria

def Agregarestudiante():
    nombre=libreria.pedir_nombre("ingrese nombre del estudiante:")
    cargo=libreria.pedir_ocupacion("ingrese ocupacion:")
    sueldo=libreria.pedir_num("ingrese notas:")
    contenido= nombre + "-" + cargo + "-" +str(sueldo) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")

def Leerestudiante():
    print("se agregaron datos")

opc=0
max=3
while(opc!=max):
    #leer el nombre,cargo,notas  de un estudiante
    print("### MENU ###")
    print("1.nombre,cargo,notas")
    print("2. leer estudiante ")
    print("3. salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if(opc==1):
        Agregarestudiante()

    if(opc==4):
        Leerestudiante()

