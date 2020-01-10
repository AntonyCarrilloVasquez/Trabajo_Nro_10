import libreria
def heladodechocolate():
    nombre=libreria.pedir_nombre("ingrese plato(helado de chocolate,arroz con leche):")
    cantidad=libreria.pedir_num("ingrese nro de platos de:")
    costo=libreria.pedir_numero("ingrese costo:",1,10)
    contenido= nombre+"-"+str(cantidad)+"-"+str(costo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

def arrozconleche():
    nombre=libreria.pedir_nombre("ingrese plato(helado de chocolate,arroz con leche):")
    cantidad=libreria.pedir_num("ingrese nro de platos de:")
    costo=libreria.pedir_numero("ingrese costo:",1,10)
    contenido= nombre+"-"+str(cantidad)+"-"+str(costo)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

opc=0
max=3
while(opc != max):
    print("#### MENU ####")
    print("1.helado de chocolate")
    print("2.arroz con leche")
    print("3.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if(opc==1):
        heladodechocolate()
    if(opc==2):
        arrozconleche()
