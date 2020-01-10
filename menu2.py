import libreria
def arrozconpollo():
    nombre=libreria.pedir_nombre("ingrese plato(ceviche,arroz con pollo):")
    cantidad=libreria.pedir_num("ingrese nro de platos de:")
    costo=libreria.pedir_numero("ingrese costo:",1,50)
    contenido= nombre+"-"+str(cantidad)+"-"+str(costo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

def ceviche():
    nombre=libreria.pedir_nombre("ingrese plato(ceviche,arroz con pollo):")
    cantidad=libreria.pedir_num("ingrese nro de platos de:")
    costo=libreria.pedir_numero("ingrese costo:",1,50)
    contenido= nombre+"-"+str(cantidad)+"-"+str(costo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

opc=0
max=3
while(opc != max):
    print("#### MENU ####")
    print("1.arroz con pollo")
    print("2.ceviche")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if(opc==1):
        arrozconpollo()
    if(opc==2):
        ceviche()
