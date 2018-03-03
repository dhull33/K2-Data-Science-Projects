#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:49:12 2018

@author: davidhull
"""
import random
import time


def validate_user_input(options, prompt, valid_inputs):
    valid_input = None
    while not valid_input:
        print(options)
        user_input = input(prompt)
        try:
            user_input = int(user_input)
        except:
            user_input = user_input.lower()

        if user_input in valid_inputs:
            valid_input = True
        else:
            print('Invalid input. Try again.')

    return user_input


class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0

    def alive(self):
        return self.health > 0

    def print_status(self):
        print('{} has {} health and {} power.'.format(self.name, self.health, self.power))

    def attack(self, enemy):
        if enemy.evade > 0 and random.random() < 0.05:
            print("You have evaded an attack!")
            print('')
        elif enemy.armor > 0:
            arm_health = enemy.health + enemy.armor
            arm_health -= self.power
            print('Your armor has protected you!')
        elif enemy.name == 'Shadow of Death' and random.random() < 0.1:
            print("The {} has dodged your attack!".format(enemy.name))
        else:
            enemy.health -= self.power
            print("")
            print("The {} has taken {} health from the {}!".format(self.name, self.power, enemy.name))
            print('')


class Hero(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Hero'
        self.health = 12
        self.power = 3
        self.coins = 10
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        if random.random() <= 0.2:
            enemy.health -= self.power
        elif self.armor > 0:
            arm_health = self.health + self.armor
            arm_health -= enemy.power
            print('Your armor has protected you!')
        super(Hero, self).attack(enemy)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def restore(self):
        self.health = 10
        print("Hero's health is restored to {}!".format(self.health))
        time.sleep(1)


class Goblin(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Goblin of Terror'
        self.health = 6
        self.power = 2
        self.bounty = 5
        self.armor = 0
        self.evade = 0


class Zombie(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Zombie of Doom'
        self.health = 100
        self.power = 1
        self.bounty = 10
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        self.health += 6
        enemy.health -= self.power
        print("The Zombie has taken {} health from you.".format(enemy.health))
        super(Zombie, self).attack(enemy)


class Medic(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Medic'
        self.health = 8
        self.power = random.randint(1, 7)
        self.bounty = 6
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        if random.randrange(1, 10, 1) <= 2:
            self.health += 2
            enemy.health -= self.power
            print("The Medic has gained {} health points!".format(self.health))
            print('')
            print("The Medic has taken {} health from you.".format(enemy.health))
        super(Medic, self).attack(enemy)


class Shadow(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Shadow of Death'
        self.health = 1
        self.power = random.randint(0, 9)
        self.count = 0
        self.bounty = 4
        self.armor = 0
        self.evade = 0


class Wizard(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Evil Wizard'
        self.health = 15
        self.power = random.randint(1, 9)
        self.bounty = 7
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        else:
            enemy.health -= self.power

        super(Wizard, self).attack(enemy)


class Godzilla(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Godzilla'
        self.health = 20
        self.power = random.randint(5, 10)
        self.bounty = 25
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        eat = random.random() > 0.01
        if eat:
            enemy.health -= (self.power * 3)
        super(Godzilla, self).attack(enemy)

###################### Battle ###########################


class Thunderdome(object):
    def pre_bat(self):
        print("==============================")
        print("  Welcome to the Thunderdome  ")
        print("==============================")
        print("            Shhh...\n  ", u"\u2620", "Death is Listening", u"\u2620")
        time.sleep(1.5)

    def battle(self, hero, enemy):
        print("")
        print("Your Potential Adversaries: \n"
              "   The Zapping Zombie \n"
              "   The Gruesome Goblin \n"
              "   The Wrecking Wizard \n"
              "   The Shocking Shadow \n"
              "   The Mummified Medic \n"
              "   Godzilla the GOAT!")
        print("")

        time.sleep(1)

        yaynay = validate_user_input("The {} challenges you!\n".format(enemy.name),
                                     "Shall we fight to the death Hero? (y/n)\n> ",
                                     ['y', 'n'])

        if 'n' in yaynay:
            time.sleep(1)
            print("You have brought great shame upon your family...")
            exit(0)

        while hero.alive() and enemy.alive():
            print("================================")
            print("Hero faces the {}!".format(enemy.name))
            print("================================")
            print('')
            hero.print_status()
            enemy.print_status()
            time.sleep(1)
            print('')
            print("-----------------------")
            keyinput = validate_user_input("1. Fight your challenger {}?\n"
                                           "2. Do nothing?\n"
                                           "3. Run away?\n".format(enemy.name),
                                           "What should you do?\n> ",
                                           [1, 2, 3])

            if keyinput == 1:
                hero.attack(enemy)
                enemy.attack(hero)

            elif keyinput == 2:
                print("")
                print("That was dumb...?")
                print("")
                enemy.attack(hero)
            elif keyinput == 3:
                print("")
                stow = validate_user_input('', "Shall we go to the store then? (y/n)\n> ", ['y', 'n'])
                if 'y' in stow:
                    return True
                print("")
                print("I am ashamed to have called you a hero!")

            else:
                print("")
                print("You are not fit to enter the Thunderdome.")
                exit(0)

        if hero.alive():
            hero.coins += enemy.bounty
            print("You have defeated the {}!".format(enemy.name))
            return True
        else:
            print("You have dishonored your ancestors.")
            return False

################## Store Items ############################


class Tonic(object):
    cost = 5
    name = 'Tonic'

    def apply(self, character):
        character.health += 5
        print("Your health has increased to {}.".format(character.health))


class SuperTonic(object):
    cost = 15
    name = 'SuperTonic'

    def apply(self, hero):
        hero.health += 15
        print("Hero's health has increased to {}.".format(hero.health))


class Sword(object):
    cost = 10
    name = 'Sword'

    def apply(self, hero):
        hero.power += 2
        print("Your power has increased to {}.".format(hero.power))


class Armor(object):
    cost = 3
    name = 'Armor'

    def apply(self, hero):
        hero.armor += 2
        print("Your armor has increased to {}!".format(hero.armor))


class Evade(object):
    cost = 12
    name = 'Evade'

    def apply(self, hero):
        hero.evade += 2
        print("You're getting pretty good at dodging attacks.\nYou have {} evade points.".format(hero.evade))


################### Store ############################


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor, Evade]

    def welcome(self):
        print("")
        print("=====================")
        print("Welcome to the store!")
        print("=====================")

    def do_shopping(self, hero):
        while True and hero.coins > 0:
            print("")
            print("You have {} coins.".format(hero.coins))
            print("")
            # print("What do you want to purchase?")
            options = ''
            for i in range(len(Store.items)):
                item = Store.items[i]
                options += "{}. buy {} ({} coins)\n".format(i + 1, item.name, item.cost)
            inp = validate_user_input(options + "10. leave",
                                      "What do you want to purchase?\n> ",
                                      list(range(len(Store.items))) + [10])
            if inp == 10:
                break

            else:
                ItemToBuy = Store.items[inp - 1]
                item = ItemToBuy()
                if hero.coins < item.cost:
                    print("You don't have enough coins.")
                    print("")
                    print("Go back to the Thunderdome and fight to earn your keep")
                    print("")
                    break

                else:
                    hero.buy(item)

        print("No coins remaining. Returning to the Thunderdome.")


if __name__ == "__main__":
    hero = Hero()

    thunderdome = Thunderdome()

    enemies = [Goblin(), Wizard(), Shadow(), Godzilla(), Medic(), Zombie()]

    shop = Store()

    thunderdome.pre_bat()
    for enemy in enemies:
        hero_won = thunderdome.battle(hero, enemy)
        if not hero_won:
            print("")
            print("What is dead may never die...")
            exit(0)
        shop.welcome()
        shop.do_shopping(hero)

    print("Congratulations! You have defeated all your enemies!")
    print("")
    print("What are going to do with all your free time?")
    exit(0)
