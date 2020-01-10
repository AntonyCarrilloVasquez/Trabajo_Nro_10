import libreria
def excelencia():
    nombre=libreria.pedir_nombre("ingrese colegio(excelencia,federico):")
    cantidad=libreria.pedir_num("ingrese nro de estudiantes de:")
    costo=libreria.pedir_numero("ingrese costo de mensualidad:",100,300)
    contenido= nombre+"-"+str(cantidad)+"-"+str(costo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

def federico():
    nombre=libreria.pedir_nombre("ingrese colegio(excelencia,federico):")
    cantidad=libreria.pedir_num("ingrese nro de estudiantes de:")
    costo=libreria.pedir_numero("ingrese costo de mensualidad:",20,50)
    contenido= nombre+"-"+str(cantidad)+"-"+str(costo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

opc=0
max=3
while(opc != max):
    print("#### MENU ####")
    print("1.excelencia")
    print("2.federico")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if(opc==1):
        excelencia()
    if(opc==2):
        federico()
