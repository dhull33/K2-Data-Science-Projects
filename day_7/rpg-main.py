#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:22:46 2018

@author: davidhull
"""
from hero_rpg import *

hero = Hero()
goblin = Goblin()
zombie = Zombie()
goblin.alive()
hero.alive()
hero.alive

while hero.alive() and goblin.alive():
    print('You have {} health and {} power.'.format(hero.health, hero.power))
    print('The zombie has {} health and {} power.'.format(zombie.health, zombie.power))
    print('The goblin has {} health and {} power.'.format(goblin.health, goblin.power))
    print()
    print('What would you like to do?')
    print('1: Fight the zombie')
    print('2: Fight the goblin')
    print('3: Observe the creatures')
    print('4: Flee')
    
    raw_input = int(input('> '))
    
    if raw_input == 1:
        # Hero fights zombie
        print("Prepare to meet your doom zombie!")
        
        hero.hero_attack(zombie)
        print("")
        print("You did {} damage to the zombie! Fuck yeah!".format(hero.damage))
        zombie.never_die
        print("")
        print("Oh no! The zombie has gained 6 health points! WTF?!?!")
        
        if zombie.alive():
            print("I AM COMING FOR YOU HERO!!!!! --ZomZom")
            zombie.attack(hero)
            print('')
            print('The zombie has taken {} health from you hero.'.format(zombie.power))
            zombie.never_die()
            print("What is dead may never die...")
            print()
        
        if hero.alive():
            pass
        else:
            print("You are a disgrace.")
        continue
        
    elif raw_input == 2:
        #Hero fights goblin
        print("Prepare to meet your doom goblin!")
        hero.hero_attack(goblin)
        print("")
        print("You did {} damage to the goblin! Fuck yeah!".format(hero.power))
        
        if goblin.alive():
            print("I AM COMING FOR YOU HERO!!!!! --GobGob")
            goblin.attack(hero)
            print('')
            print('The goblin has taken {} health from you hero.'.format(goblin.power))
            print('')
        else:
            print("You have defeated the goblin!!\nThe realm is finally at peace thanks to your bravery.")
            
        if hero.alive():
            pass
        else:
            print("You are a disgrace.")
        
          
        
            
    elif raw_input == 3:
        print("They are interesting creatures indeed...")
    
    
    elif raw_input == 4:
        print("You have brought shame upon your family.")
        break
    
    else:
        print("Invalid input {}".format(raw_input))
        print("")
        print("You do not deserve to embark upon this quest.")
        break
    
    
