print("Bienvenido al juego 'PIEDRA, PAPEL O TIJERA'")
print("--------------------------------------------")

import random #Se importa el random para la eleccion del computador

opciones= ("piedra", "papel", "tijera")
repetir= "si"


while repetir == "si": #este while nos sirve para saber si se desea juguar otra vez (por defecto empieza como SI)
    elecUsuario= input("Elige: Piedra, Papel o Tijera:\n")
    elecUsuario= elecUsuario.lower()
    while elecUsuario!= "piedra" and elecUsuario!= "papel" and elecUsuario!= "tijera": #Este while es para asegurarse que se escoja una respuesta existente
        print("Opcion Incorrecta.")
        elecUsuario= input("Elige: Piedra, Papel o Tijera:\n")
        elecUsuario= elecUsuario.lower()
        

    elecCompu= random.choice(opciones) #el computador usa random para escoger su respuesta aleatoria
    print("El computador escogió: **",elecCompu,"**")

    if elecUsuario == elecCompu:#si la eleccion del compuutador y del usuario son iguales, pues entra en el if
        print("EMPATE, Casi lo logras\n")
    elif (elecUsuario =="piedra" and elecCompu =="tijera") or (elecUsuario =="tijera" and elecCompu =="papel") or(elecUsuario =="papel" and elecCompu=="piedra"): #si no fue empate va a ver si ganó el jugador con cualquiera de las posibilidades
            print("Felicidades, GANASTE!\n")
    else: #si no ganó ni fue empate lo unico que queda es que haya perdido
        print("PERDISTE :( , Mejor suerte la proxima\n")
    
    repetir=input("¿Jugar otra vez? Si/No:").lower() 
    while repetir != "si" and repetir!= "no": #valida si se agrego una respuesta correcta
        print("Opcion Incorrecta.")
        repetir= input("¿Jugar otra vez? Si/No:\n")
        repetir= repetir.lower()
    
print("Esta bien, Hasta luego!")
