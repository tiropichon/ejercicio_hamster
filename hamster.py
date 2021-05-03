# -*- coding: utf-8 -*-

# Escribe aquí tu código
def mostrar_menu():
    #Creo un diccionario con los datos de mi mascota
    hamster={"name":"Toni","age":5,"weight":12.0,"hungry":False,"mood":"happy","photo":"<:3)---"}
    hamster2={"name":"","age":0,"weight":0.0,"hungry":False,"mood":"","photo":""}
    
    
    #Inicializo la variable opcion a 1 para que el bucle while se ejecute al 
    #menos 1 vez
    opcion = 1
    
        
    #Muestro el menú, hasta q se introduzca el 0
    while opcion != 0:
        print("Opciones")
        print("========")
        print("1 -> Mostrar datos de mi mascota")
        print("2 -> Poner valores iniciales de 'hungry' en 'True' y de 'Mood' en 'Sad'")
        print("3 -> Alimentar a la mascota")
        print("4 -> Jugar con la mascota")
        print("5 -> Crear una nueva mascota")
        print("6 -> Alimentar a las mascotas con un bucle de iteración")
        print("--------------------------")
        print("0 -> Salir")
        opcion=int(input("Introduce opción:"))
        if (opcion == 1):   
            #Muestro los datos de mi mascota
            mostrar_datos(hamster)
        
        if (opcion == 2):  
            #Cambio valores 'hungry' a True y 'mood' a 'Sad
            cambiar_valores(hamster)
        
        if (opcion == 3):    
            #Alimento una mascota. Pido el nombre.
            nmascota = str(input("Introduce nombre de la mascota a alimentar: "))
            feed(nmascota,hamster)
        
        if (opcion == 4):
            #Juego con la mascota
            play(hamster)
        
        if (opcion == 5):
            #creo una nueva mascota
            crear_mascota(hamster2)
                
        if (opcion == 6):
            #alimento las mascotas con un bucle de iteración
            alimentar_mascotas(hamster,hamster2)
    return


def feed(nombre, hamster):
    
    if nombre in hamster.values():
        if hamster["hungry"] == False:
            print(f"La mascosa {hamster['name']} no tiene hambre\n")
        else:
            hamster["hungry"] = False
            hamster["weight"] += 0.1 
            mostrar_datos(hamster)
    else:
        print("Ese nombre de mascota no existe.\n")
    return hamster

def mostrar_datos(hamster):
    
    #Presento mi mascota y la describo
    print("Datos de mi mascota")
    print("-------------------")
    print(f"Nombre: {hamster['name']}")
    print(f"Edad: {hamster['age']}")
    print(f"Peso: {hamster['weight']}") 
    if hamster["hungry"] == False:
        print("Hambriento: No")
    else:
        print("Hambriento: Sí")
    if hamster["mood"] == "sad" or hamster["mood"] == "Sad":
        print("Estado de ánimo: Triste")
    else:
        print("Estado de ánimo: Feliz")
    print(f"Foto: {hamster['photo']} \n")
    
def mostrar_datos_masc2(hamster2):
    
    #Presento mi mascota y la describo
    print("Datos de mi mascota")
    print("-------------------")
    print(f"Nombre: {hamster2['name']}")
    print(f"Edad: {hamster2['age']}")
    print(f"Peso: {hamster2['weight']}") 
    if hamster2["hungry"] == False:
        print("Hambriento: No")
    else:
        print("Hambriento: Sí")
    if hamster2["mood"] == "sad" or hamster2["mood"] == "Sad":
        print("Estado de ánimo: Triste")
    else:
        print("Estado de ánimo: Feliz")
    print(f"Foto: {hamster2['photo']} \n")
    return

def cambiar_valores(hamster):
    
    hamster["hungry"] = True
    hamster["mood"] = "sad"
    mostrar_datos(hamster)
    return hamster


def crear_mascota(hamster2):
    
    
    print("Datos nueva mascota")
    print("===================")
    nombre_masc = str(input("Nombre mascota:"))
    edad_masc = int(input("Edad:"))
    peso_masc = float(input("Peso:"))
    pedir_hamb = True
    while (pedir_hamb == True):
        hambriento = str(input("¿Esta hambriento? (s/n):"))
        if (hambriento == "S" or hambriento == "s" or 
            hambriento == "N" or hambriento == "n"):
           if (hambriento == 'S' or hambriento == 's'):
               hambre_masc = True
               pedir_hamb = False 
           else:
               hambre_masc = False
               pedir_hamb = False 
        else:
            pedir_hamb = True
    
    pedir_mood = True
    while(pedir_mood == True):
        animo=str(input("¿La mascota esta feliz? (s/n):"))
        if (animo == "S" or animo == "s" or animo == "N" or animo == "n"):
            if(animo == "S" or animo == "s"):
                animo_masc="happy"
                pedir_mood = False 
            else:
                animo_masc="sad"
                pedir_mood = False 
        else:
            pedir_mood = True
            
    foto_masc = str(input("Foto de la mascota:"))
    hamster2["name"]=nombre_masc
    hamster2["age"]=edad_masc
    hamster2["weight"]=peso_masc
    hamster2["hungry"]=hambre_masc
    hamster2["mood"]=animo_masc
    hamster2["photo"]=foto_masc
    
    #hamster2={"name":nombre_masc,"age":edad_masc,"weight":peso_masc,
    #          "hungry":hambre_masc,"mood":animo_masc,"photo":foto_masc}
    mostrar_datos_masc2(hamster2)
    return hamster2

def alimentar_mascotas(hamster, hamster2):
    
    #recorro el diccionario hamster.
    for k,y in hamster.items():
            #Asigno False al elemento "hungry"
            if str(k) == "hungry": 
                y = False 
            
            #Asigno al elemento "weight", el peso + 0.1
            if str(k) == "weight":
                y += 0.1
    mostrar_datos(hamster)
    
    #recorro el diccionario hamster2.
    if len(hamster2) > 0:
        for k,y in hamster2.items():
            #Asigno False al elemento "hungry"
            if str(k) == "hungry": 
                y = False
            
            #Asigno al elemento "weight", el peso + 0.1
            if str(k) == "weight":
                y += 0.1
        mostrar_datos_masc2(hamster2)
      
    return hamster, hamster2

def play(hamster):
    
    #asigno a la mascota los valores "mood" -> feliz, 
    #y el peso -> peso - 0.2
    hamster["mood"]="happy"
    hamster["weight"] -= 0.2
    
    #Si el peso es menor a 11.9, establece estado "hungry" a True
    #Y muestra un mensaje que la mascota está cansada y hambrienta
    if (hamster["weight"] < 11.9):
        hamster["hungry"] = True
        print("---> La mascota está cansada y hambrienta. Peso por debajo de 11.9 <--- \n")
    
    mostrar_datos(hamster)
    return hamster   
    
#main
#llamo a la función que va a mostrar el menú por pantalla.
mostrar_menu()
