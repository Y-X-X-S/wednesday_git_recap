import random

options = ["piedra", "tijera", "papel"]

print("Hola,juguemos cachipun")

print ("Ingresa su opción")
print (1, "piedra")
print (2, "tijera")
print (3, "papel")

user_input = int(input("jugador1\n"))
user_option = options[user_input - 1]

computer_option = random.choice(options)

print("Mi mano: ", user_option)
print("Mano del computador:", computer_option)

if (user_option == computer_option):
  print("Empatan jugadores")

elif (user_option == "piedra" and computer_option == "tijera") or(user_option == "tijera" and computer_option == "papel") or (user_option == "papel" and computer_option == "piedra"):
  print("Felicitaciones! ganaste la partida")
    
else:
    print("Lo siento! el computador ha ganado")