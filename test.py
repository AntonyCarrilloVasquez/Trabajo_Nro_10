import libreria
assert (libreria.validar_numero("hola")== False)
assert (libreria.validar_numero(13456)== True)
assert (libreria.validar_numero(1)== True)
assert (libreria.validar_numero("Juan")== False)
print("validar_numeero ok")

assert (libreria.validar_nombre("juan")==True)
assert (libreria.validar_nombre("antony")==True)
assert (libreria.validar_nombre(12)==False)
print("validar nombre ok")

assert (libreria.validar_apellido("coronado")==True)
assert (libreria.validar_apellido("virgilio")==True)
assert (libreria.validar_apellido(123)==False)
print("validar nombre ok")
