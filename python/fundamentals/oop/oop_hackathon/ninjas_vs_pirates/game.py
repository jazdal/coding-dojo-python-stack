import random
import os
from classes.ninja import *
from classes.pirate import *

round = 1

def cls():
    os.system('cls')

def prompt():
    print()
    input('Press Enter to continue...')
    cls()

ninja_class = [Ninja, Shinobi]
pirate_class = [Pirate, Corsair]

cls()
print('WELCOME TO NINJAS 🥷  VS. PIRATES 🏴‍☠️  !!!')
prompt()

print('One day, a Ninja and a Pirate were kidnapped')
print('from their hometowns and marooned in an island...')
prompt()

player1 = random.choice(ninja_class)(input("Enter Ninja name: "))
print()
player2 = random.choice(pirate_class)(input("Enter Pirate name: "))
prompt()

print('In order to escape the island, ')
print('the Ninja and the Pirate must fight each other')
print('until one of them falls!!!')
prompt()

while player1.health > 0 and player2.health > 0:
    print(f'ROUND {round}!')
    print()

    if round == 1:
        print(f'In the Ninja Corner, we have {player1.name.upper()} 🥷   !!!')
        print()
        print(f'And in the Pirate Corner, we have {player2.name.upper()} 🏴‍☠️   !!!')
        prompt()

    print(f'Get ready to fight...')
    prompt()

    print(f'FIGHT!!! 🥷  🥊 🏴‍☠️  ')
    prompt()

    attacker = random.randint(1,2)

    if attacker == 1:
        print(f'{player1.name} attacks {player2.name}!')
        player1.determine_technique()

        if player1.technique == 1:
            player1.attack(player2)
            print()
            player2.show_stats()
            prompt()
        
        elif player1.technique == 2:
            player1.shuriken_strike(player2)
            print()
            player2.show_stats()
            prompt()
        
        elif player1.technique == 3:
            player1.sword_slash(player2)
            print()
            player2.show_stats()
            prompt()
    
    elif attacker == 2:
        print(f'{player2.name} attacks {player1.name}!')
        player2.determine_technique()

        if player2.technique == 1:
            player2.attack(player1)
            print()
            player1.show_stats()
            prompt()
        
        elif player2.technique == 2:
            player2.hook_hand(player1)
            print()
            player1.show_stats()
            prompt()
        
        elif player2.technique == 3:
            player2.cannonball(player1)
            print()
            player1.show_stats()
            prompt()

    round += 1

if player1.health <= 0 or player2.health <= 0:
    winner = player1 if player1.health > 0 else player2

    print(f'The fight is over after {round} rounds!')
    prompt()
    print(f'The winner of the fight is... the {winner.__class__.__name__} {winner.name.upper()}!!!')