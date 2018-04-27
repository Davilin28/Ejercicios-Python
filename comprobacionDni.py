correcto = True

while correcto == True:
    
    dni=input("Ingrese su dni con la letra y separado con un guion:\n")
    separador           = dni.split("-")
    numeros             = separador[0]
    letra               = separador[1]
    letrasmayusculas    = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    letrasminusculas    = ["t","r","w","a","g","m","y","f","p","d","x","b","n","j","z","s","q","v","h","l","c","k","e"]

    for minusculas in letrasminusculas:
        if separador[1] == minusculas:
            numeros = int(numeros)
            resto = numeros % 23
            if letrasminusculas[resto] == letra:
                print("El dni " + dni + " es correcto.\n")
                correcto=False
            else:
                print("El dni " + dni + " es falso.\n")
                correcto==True

            
    for mayusculas in letrasmayusculas:
        if separador[1] == mayusculas:
            numeros = int(numeros)
            resto = numeros % 23
            if letrasmayusculas[resto] == letra:
                print("El dni " + dni + " es correcto.\n")
                correcto=False
            else:
                print("El dni " + dni + " es falso.\n")
                correcto==True
