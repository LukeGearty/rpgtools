from player import *
import sys
import random

"""

Enter the Distant Tombs and find the treasure within! Enter first with just your wits about you, find the weapon hidden within, slay the monster guarding the treasure.

"""


#first the player creates their character

#Then the player enters the tomb and can choose to go left or right

#if the player goes left, then they come across a trap, but they can get the weapon, a magical spear that always hits the target and returns to the player's hand after, they need if they survive the trap

#if the player goes right, then they come across the treasure, and the Minotaur guarding the treasure. The player gets into a fight with the minotaur.

#If the player has the Spear of Return, then the fight is much easier. If not, then the player will most surely lose (but can win if they are lucky)


PLAYER_HEALTH = 100


has_weapon = False
visited_left = False
visited_right = False
completed_game = False
has_treasure = False



def create_character(name: str, vocation: str):
    if vocation == "Warrior":
        player_weapon = Weapon("Sword", 25)
    elif vocation == "Thief":
        player_weapon = Weapon("Bow and Arrow", 15)
    elif vocation == "Mage":
        player_weapon = Weapon("Staff", 10)
    
    player_class = Archetype(name, vocation, PLAYER_HEALTH)
    player_character = Player(player_class, player_weapon)

    return player_character



def enter_tomb(character):

    print(f"Welcome {character.name} to the Distant Tombs! In here you will find treasure and adventure\n")
    print("You find yourself in front of a gargantuan tomb, with a statue of an old and ancient warrior out front. You bravely walk forward into the tomb, lighting a torch to see in the dark.")
    print("You find yourself in a small room, filled with dirt and dust. Rats scatter as your light illuminates the room.")

    main_room(character)



def main_room(character):
    global completed_game

    try:
        while completed_game == False:
            print("There are two possible ways forward in the room. One to the left, and one to the right. Which one do you take?")
            print("1. Left")
            print("2. Right")
            choice = int(input())

            if choice == 1:
                if visited_left == False:
                    print("You go to the left, towards uncertain adventure")
                else: 
                    print("You go to the left, towards the trap that nearly took your life")
                left_room(character)
            elif choice == 2:
                if visited_right == False:
                    print("You go to the right, towards uncertain adventure")
                else:
                    print("You go to the right, toward the room with the minotaur")
                right_room(character)
            else:
                print("You leave the tomb, you coward")
                completed_game = True
                return
    except ValueError:
        print("You are a dunce, and you turn around and hit your head and die. The torch lights you on fire, and the rats eat your charred remains")
        completed_game = True
        character.is_alive = False
        return



def left_room(character):
    global visited_left
    global completed_game
    global has_weapon


    if visited_left == False:
        visited_left = True
        print("You come across a large room with nothing really in it except for a large altar. On the altar is a spear, emanating light from the spearhead. You recognize it as the Spear of Return, a powerful weapon. This is not the treasure of the Distant Tombs, but it is an amazing discovery")
        print("You walk forward and trigger a trap! Arrows start raining down from everywhere. You weave and you dodge to reach the spear")
        damage = random.randint(1, 50)
        character.take_damage(damage)

        if character.is_alive:
            print(f"{character.name}, you dodged the arrows and only took {damage} damage! You manage to get the Spear of Return! You return back to the main room.")
            has_weapon = True
        else:
            print(f"{character.name}, you perish in the trap, having taken {damage} damage by the never ending barrage of arrows, never reaching the Spear of Return")
            print("Your corpse is doomed to stay in the Distant Tombs until a new adventurer finds you.")
            completed_game = True
        return
    else:
        print("You have everything you need from this room")
        return
    


def right_room(character):
    global visited_right, completed_game, has_treasure, has_weapon
    
    if visited_right == False:
        visited_right = True

        print("You come across the magical treasure chest, being guarded by a minotaur with a massive battleaxe!")
        print("He spots you, and charges at you!")

        if has_weapon:
            print("You ready the Spear of Return, and throw it at the charging minotaur")
            player_damage = random.randint(5000, 100000)

            print(f"The Spear of Return penetrates the minotaur's exposed chest, and does {player_damage} damage to the minotaur! He falls down and perishes")

            print("You walk over his corpse and claim your prize, the famed treasure of the Distant Tombs")
            has_treasure = True
            completed_game = True
        else:
            print(f"You ready your weapon, your trusted {character.weapon}, and attack the charging minotaur")
            print(f"You manage to do a respectable {character.damage} damage to the minotaur")

            print("His turn.")

            minotaur_damage = random.randint(0, 100)
            print(f"He does {minotaur_damage} damage to you")

            character.take_damage(minotaur_damage)

            if character.is_alive:
                print("You can go back, or continue to fight. What do you want to do?")
                print("1. Go Back")
                print("2. Fight")

                try:
                    choice = int(input())
                    if choice == 1:
                        print("You go back")
                        return
                    elif choice == 2:
                        print(f"You ready your {character.weapon} and do another {character.damage} damage to the minotaur.")
                        print("He looks at you with a look that says 'Are you kidding me', he readies his massive battleaxe, and it comes crashing down on you")
                        second_minotaur_hit = random.randint(10000, 1000000)
                        print(f"It hits you with the force of 10,000 earthquakes. You see your entire life flash before your eyes. It does {second_minotaur_hit} damage to you.")

                        character.take_damage(second_minotaur_hit)

                        print("It hits you so hard that your ancestors are rattling around in heaven. You are now more of a puddle of blood and organs, rather than the human being you once were. The minotaur spends the next week cleaning your remains from his battleaxe.")
                        character.is_alive = False
                        completed_game = True
                        return
                    else:
                        print("The minotaur kills you, because you cannot follow directions")
                        character.is_alive = False
                        completed_game = True
                        return
                except ValueError:
                    print("The minotaur kills you, because you cannot follow directions")
                    character.is_alive = False
                    completed_game = True
                    return
            else:
                print("You fought heroically, but you're dead. Congratulations.")
                character.is_alive = False
                completed_game = True
                return
    else:
        print("You see the massive minotaur, the feeling of what he had done to you before still on your mind, and are wondering if this is what it is like to face down death.")

        if has_weapon:
            print("You ready the Spear of Return, and throw it at the charging minotaur")
            player_damage = random.randint(5000, 100000)

            print(f"The Spear of Return penetrates the minotaur's exposed chest, and does {player_damage} to the minotaur! He falls down and perishes")

            print("You walk over his corpse and claim your prize, the famed treasure of the Distant Tombs")
            has_treasure = True
            completed_game = True

            return
        else:
            print("The minotaur lifts you up by the neck and slowly chokes the life out of you. You see your life flash before your eyes as you die.")
            character.is_alive = False
            completed_game = True



def main():
    name = input("Enter your character name: ")
    vocation_choices = ["Mage", "Warrior", "Thief"]

    for i in range(len(vocation_choices)):
        print(f"{i + 1}: {vocation_choices[i]}")
    
    try:
        proper_choices = [1, 2, 3]
        choice = int(input("Enter your character class: "))

        while choice not in proper_choices:
            print("Pick a real choice, you dunce")
            choice = int(input("Enter your character class: "))
    except ValueError:
        print("If you don't want to play, that's fine!")
        sys.exit()

    player_class = vocation_choices[choice - 1]
    character = create_character(name, player_class)
    
    enter_tomb(character)

    if character.is_alive and has_treasure:
        print("You look through your treasure and realize you are about to be rich!")
    elif character.is_alive == False:
        print(f"You're dead. Sorry, the heroic tale of {character.name} has reached it's end")
    else:
        print("You leave the tomb, forever wondering what would've happened had you stayed")
    sys.exit()

    print("Thank you for playing!")




if __name__=="__main__":
    main()