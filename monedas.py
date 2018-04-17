#Variables
billetes = dict()

billetes = {
    50:1,
    20:0,
    10:3,
    5:4,
    2:10,
    1:10,
    0.5:3,
    0.2:0,
    0.1:10,
    0.05:3,
    }

#Funciones
def contar(billetes):
    print("\n\tDinero Actual:\n")
    
    for key in sorted(billetes):
        print("\t%s€ - %i cantidad" %(key,billetes[key]))
    print("\n")
    
#Menu
def menu():
    print ("Selecciona una opción")
    print ("\t1 - Consultar dinero")
    print ("\t2 - Dar cambio")
    print ("\t3 - Reponer cambio")
    print ("\t4 - Guardar estado")
    
while True:
        menu()
        opcionMenu = input("\n Elige una opcion: ")

        if opcionMenu=="1":
            contar(billetes)
        elif opcionMenu=="2":
            print("2")
        elif opcionMenu=="3":
            print("3")
        elif opcionMenu=="4":
            print("4")


