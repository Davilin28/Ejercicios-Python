import comprobacion

correcto = True

while correcto == True:
    
    contrasena          = input("Ingrese su contrasena: ")
    validador           = contrasena
    repetirContra       = input("Por favor ingrese de nuevo la contrasena anterior: ")
    validadorRepetido   = repetirContra

    if comprobacion.clave(validador,validadorRepetido)  ==  True:
        print("Contrasena Aceptada")
        correcto = False
    
