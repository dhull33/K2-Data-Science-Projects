#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:49:12 2018

@author: davidhull
"""
import random
import time
import re



class InputManager(object):
    """Class with methods for sanitizing user input."""
    def __init__(self):
        pass


    def get_yes_or_no(prompt):
        """Sanatizes user input for yes or no questions.

        Args:
            prompt: the question displayed to the user.

        Returns:
            Bool - True for yes answer, False for No Answer."""

        while True:
            print(prompt)
            ans = input("> ")
            if ans[0].lower() == "y":
                return True
            elif ans[0].lower() == "n":
                return False
            else:
                print("That's not a valid answer, bud.")


    def get_numerical_input(prompt, num_options, extra_option=None):
        """Sanatizes user input when chosing between multiple options.

        Args:
            prompt: the question displayed to the user
            num_options: the amount of options the user has to chode between.
            extra_options: optional arguement if there is an extra argument
            outside of 'num_options'

        Returns:
            ans: sanitised answer to the prompt."""
        while True:
            print(prompt)
            try:
                ans = int(input("> "))
            except ValueError:
                print("You need to enter a number, fella.")
                continue
            if not extra_option:
                if re.match(f"^[1-{str(num_options)}]$", str(ans)):
                    return ans
                else:
                    print("That's not a valid answer, bud.")
            else:
                if re.match(f"^[1-{str(num_options)}]$", str(ans)):
                    return ans
                if ans == extra_option:
                    return ans
                else:
                    print("That's not a valid answer, bud.")




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
            pass
        elif enemy.armor > 0:
            arm_health = enemy.health + enemy.armor
            arm_health -= self.power
            print('Your armor has protected you!')
        elif enemy.name == 'Shadow of Death' and random.random() < 0.1:
            print("The {} has dodged your attack!".format(enemy.name))
            pass
        else:
            enemy.health -= self.power
            print("")
            print("The {} has taken {} health from the {}!".format(self.name, self.power, enemy.name))
            print('')




class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 12
        self.power = 3
        self.coins = 10
        self.armor = 0
        self.evade = 0


    def attack(self, enemy):
        if random.random() <= 0.2:
            enemy.health -= self.power * 2
        elif self.armor > 0:
            arm_health = self.health + self.armor
            arm_health -= enemy.power
            print('Your armor has protected you!')
        super(Hero, self).attack(enemy)


    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def restore(self):
        self.health = 10
        print("Hero's health is restored to {}!".format(self.health))
        time.sleep(1)



class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin of Terror'
        self.health = 6
        self.power = 2
        self.bounty = 5
        self.armor = 0
        self.evade = 0

class Zombie(Character):
    def __init__(self):
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
        self.name = 'Shadow of Death'
        self.health = 1
        self.power = random.randint(0, 9)
        self.count = 0
        self.bounty = 4
        self.armor = 0
        self.evade = 0



class Wizard(Character):
    def __init__(self):
        self.name = 'Evil Wizard'
        self.health = 15
        self.power = random.randint(3, 9)
        self.bounty = 7
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack!".format(self.name, enemy.name))

            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)

class Godzilla(Character):
    def __init__(self):
        self.name = 'Godzilla'
        self.health = 20
        self.power = random.randint(5, 10)
        self.bounty = 25
        self.armor = 0
        self.evade = 0

    def attack(self, enemy):
        eat = random.random() > 0.01
        if eat:
            enemy.health -= (self.power * 1.5)
        super(Godzilla, self).attack(enemy)


###################### Battle ###########################

class Thunderdome(object):
    def __init__(self):
        pass


    def pre_bat(self):
        """Flavor text welcoming the user to the Thunderdome.

        Args:
            None

        Returns:
            None"""

        print("==============================")
        print("  Welcome to the Thunderdome  ")
        print("==============================")
        print("            Shhh...\n  ",u"\u2620", "Death is Listening",u"\u2620")

        time.sleep(1.5)


    def print_pre_battle_prompt(self):
        """Prints the list of adversaries the user will face when entering the
        Thunderdome.

        Args:
            None

        Returns:
            None"""

        adversaries = ["The Zapping Zombie", "The Gruesome Goblin",
                       "The Wrecking Wizard", "The Shocking Shadow",
                       "The Mummified Medic", "Godzilla the Grim!"]
        print("")
        print("Your Potential Adversaries: ")
        for adversary in adversaries:
            print("  {}".format(adversary))
        print("")

        time.sleep(1)


    def decide_if_battle(self, enemy):
        """Asks the user if they would like to do battle with the current enemy.
        Exits the program if the user does not wish to fight.

        Args:
            enemy: The enemy object the hero is battling against.

        Returns:
            None"""

        print("The {} challenges you!".format(enemy.name))
        print("")
        yay_nay = InputManager.get_yes_or_no("Shall we fight to the death Hero?(y/n)")

        if yay_nay:
            return
        else:
            time.sleep(1)
            print("You have brought great shame upon your family...")
            exit(0)


    def print_battle_data(self, hero, enemy):
        """Displays information about the current status of the battle the hero
        is in.

        Args:
            hero: A hero object controlled by the player.
            enemy: The enemy object the hero is battling against.

        Returns:
            None"""

        print("================================")
        print("Hero faces the {}!".format(enemy.name))
        print("================================")
        print('')
        hero.print_status()
        enemy.print_status()
        time.sleep(1)
        print('')
        print("-----------------------")


    def decide_hero_action(self, hero, enemy):
        """Displays player's options in battle on screen and allows user to input
        their decision.

        Args:
            hero: A hero object controlled by the player.
            enemy: The enemy object the hero is battling against.

        Returns:
            hero_action(int): Interger value corresponding to the choice the
            the player made during battle."""

        fight_options = [f"1. Fight your challenger, {enemy.name}",
                         "2. Do nothing?", "3. Run Away"]
        for option in fight_options:
            print(option)
        hero_action = InputManager.get_numerical_input("What should you do?",len(fight_options))
        return hero_action


    def resolve_hero_action(self, hero, enemy, hero_action):
        """Resolves the decision made by the hero during a turn in battle.

        Args:
            hero: A hero object controlled by the player.
            enemy: The enemy object the hero is battling against.
            hero_action(int): An integer that corresponds to a choice the user
            made during the current turn in battle.

        Returns:
            Bool: True if the hero is still in combat. False if the hero has
            fled from battle."""

        if hero_action == 1:
            hero.attack(enemy)
            enemy.attack(hero)
            return True
        elif hero_action == 2:
            print("")
            print("That was dumb...?")
            print("")
            enemy.attack(hero)
            return True
        else:
            print("Running away... ...")
            return False


    def post_battle_text(self, hero, enemy, shop):
        """Displays post-battle information to the user. Gives the player the
        option to go to the store if they are still alive.

        Args:
            hero: A hero object controlled by the player.
            enemy: The enemy object the hero is battling against.
            shop: The shop object, called after the battle to allow the hero
            to shop.

        Returns:
            Bool: True if the hero is alive. False if the hero has died."""

        print("The battle has ended...")

        if hero.alive() and not enemy.alive():
            hero.coins += enemy.bounty
            print("You have defeated the {}!".format(enemy.name))
            print("")
            print("You have {} coins.".format(hero.coins))

        elif hero.alive() and enemy.alive():
            print("You are safe, for now.")
        else:
            print("You have perished.")
            return False

        go_to_store = InputManager.get_yes_or_no("Shall we go to the store then? (y/n)")
        if go_to_store:
            shop.welcome()
            shop.do_shopping(hero)
        else:
            print("")
            print("Fool! Get Ready to face your next opponent.")

        return True


    def battle(self, hero, enemy, shop):
        """Main battle loop for the Thunderdome class. Handles battle logic.

        Args:
            hero: A hero object controlled by the player.
            enemy: The enemy object the hero is battling against.
            shop: The shop object, called after the battle to allow the hero
            to shop.

        Returns:
            Bool: True is the hero is still alive. False if the hero has died."""

        self.print_pre_battle_prompt()
        self.decide_if_battle(enemy)

        while hero.alive() and enemy.alive():
            self.print_battle_data(hero, enemy)
            hero_action = self.decide_hero_action(hero, enemy)
            still_in_battle = self.resolve_hero_action(hero, enemy, hero_action)
            if not still_in_battle:
                break

        hero_alive = self.post_battle_text(hero, enemy, shop)
        if hero_alive:
            return True
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

        while True:
            print("")
            print("You have {} coins.".format(hero.coins))
            print("")
            for i, item in enumerate(Store.items):
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            inp = InputManager.get_numerical_input("What do you want to purchase?", len(Store.items), extra_option=10)
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


################### Main ##########################


def main():

    hero = Hero()

    thunderdome = Thunderdome()

    enemies = [Goblin(), Wizard(), Shadow(), Godzilla(), Medic(), Zombie()]

    shop = Store()

    thunderdome.pre_bat()
    for enemy in enemies:
        hero_won = thunderdome.battle(hero, enemy, shop)
        if not hero_won:
            print("")
            print("What is dead may never die...")
            exit(0)

    print("Congratulations! You have defeated all your enemies!")
    print("")
    print("What are going to do with all your free time?")
    exit(0)




if __name__ == "__main__":
    main()
