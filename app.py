def wanaplay():
  k=input('Do you want to play again?: ')
  if k[0].lower() in 'ys':
      play()
  else:
      print('Thankyou for playing!')
import numpy as np
import time
def uniform(n, m):
  return np.random.randint(1, n + 1, size=m)
car_door = None
goat1_door = None
goat2_door = None
choice = None
other_closed_door = None
emodict = {'door':'🚪','goat':'🐐','car':'🚗','lock':'🔒'}
d1 = emodict['door']
d2 = emodict['door']
d3 = emodict['door']
def emoex(num,emoj):
  global d1
  global d2
  global d3
  if num == 1:
    d1 = emodict[emoj]
  elif num == 2:
    d2 = emodict[emoj]
  elif num == 3:
    d3 = emodict[emoj]
def arrange():
  global car_door
  global goat1_door
  global goat2_door
  car_door = uniform(3, 1)
  if car_door == 1:
    goat1_door = 2
    goat2_door = 3
  elif car_door == 2:
    goat1_door = 1
    goat2_door = 3
  else:
    goat1_door = 1
    goat2_door = 2
def selec():
  global choice
  global other_closed_door
  global car_door
  global goat1_door
  global goat2_door
  choice = int(input('Which door you want to choose? (1/2/3): '))
  emoex(choice,'lock')
  if choice == goat1_door:
    host_reveal_door = goat2_door
    other_closed_door = car_door
  elif choice == goat2_door:
    host_reveal_door = goat1_door
    other_closed_door = car_door
  else:
    host_reveal_door = goat1_door
    other_closed_door = goat2_door
  return host_reveal_door
def winorloss():
  emoex(goat1_door,'goat')
  emoex(goat2_door,'goat')
  emoex(car_door,'car')
  print(' '*12 + f'{d1}   {d2}   {d3}')
  print(' '*12 + '[1]  [2]  [3]')
  if choice == car_door:
    print('Wooh, You selected car! :-) unfortunately this is a simulation.')
    wanaplay()
  else:
    print('Oops, You selected goat... No worries, this is a simulation :-)')
    wanaplay()
#Main code
def play():
    global d1
    global d2
    global d3
    d1 = emodict['door']
    d2 = emodict['door']
    d3 = emodict['door']
    global choice
    print('\nWelcome to Monty Hall\n NOTE: {give replies in 1,2,3 or y/n}\n')
    print('Please wait, while I arrange doors. . . .\n\n')
    time.sleep(3)
    arrange()
    print(' '*12+f'{d1}   {d2}   {d3}')
    print(' '*12+'[1]  [2]  [3]')
    temp = selec()
    emoex(temp,'goat')
    print(f'You selected door {choice}.')
    print('Hmmm m m m m',end='')
    for i in 'mmmm.......':
        print(i,end=' ')
        time.sleep(0.2)
    print()
    print(f'I\'ll open door {temp}\n\n')
    print(' '*12+f'{d1}   {d2}   {d3}')
    print(' '*12+'[1]  [2]  [3]')
    temp = input('Do you want to switch to another not opened door? (y/n): ')
    if temp != 'n':
        emoex(choice,'door')
        choice = other_closed_door
        emoex(choice,'lock')
        print(f'Your new selection is door {int(choice)}\n')
        print(' '*12+f'{d1}   {d2}   {d3}')
        print(' '*12+'[1]  [2]  [3]')
        print('Okay then, Let\'s check your luck\n\n')
        time.sleep(3)
        winorloss()
    else:
        print('Okay then, Let\'s check your luck\n\n')
        time.sleep(3)
        winorloss()
play()
