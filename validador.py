import contra

correcto=True

while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if contra.clave(contrasenia)==True:
        print("Contraseña Aceptada")
        correcto=False
