# Juego de piedra papel o tijera
import random


def jugar():
  user = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
  
  cpu = random.choice(['pi','pa','ti'])
  if user == cpu:
    return print(f'¡Empate! usuario escoge: {user} y cpu escoge: {cpu}')

  if user_won(user, cpu):
    return print(f'¡Ganaste! usuario escoge: {user} y cpu escoge: {cpu}')

  return print(f'¡Perdiste! usuario escoge: {user} y cpu escoge: {cpu}')


def user_won(player, opponent):
  # Retorna True si gana el jugador
  if ((player == 'pi' and opponent == 'ti') or 
      (player == 'pa' and opponent == 'pi') or 
      (player == 'ti' and opponent == 'pa')):
    return True
    
  else:
    return False
    

print(jugar())


