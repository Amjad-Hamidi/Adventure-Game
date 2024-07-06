# You can use this workspace to write and submit your adventure game project.
import time
import random


def print_pause(msg):
    print(msg)
    time.sleep(2)



def cave(item, enemy):
    if "sword" in item:
        print_pause("You've been here before, and you have taken"
                    " a better weapon. so you don't have to enter the cave"
                    " again.")
        print_pause(" go back to the field and choose again")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It's a small cave, there is a weapon somewhere")
        print_pause("Search for it behind the rocks.")
        print_pause("You have found the magical Sword ")
        print_pause("Now pick it up and throw the dagger away"
                    " it's more effective")
        print_pause("Go back to the field ")
        item.append("sword")
    field(item, enemy)



def introduction(item, enemy):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")



def play_again():
    again = input("Would you like to play again? (y / n)").lower()
    if again == "y":
        print_pause("Excellent! Restarting the game ")
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def house(item, enemy):
    print_pause("You approach the door of the house.")
    print_pause("Knock the door of the house "
                f"oops,it's {enemy} .")
    print_pause(f"Eep! This is the {enemy}'s house")
    print_pause(f"The {enemy} is attacking you!")
    if "sword" not in item:
        print_pause(f"Your weapon is not powerful enough to kill the {enemy},"
                    "It deppends on you ")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "sword" in item:
                print_pause(f"As the {enemy} moves to attack, "
                            "pull your sword up, stand stiddy")
                print_pause("It's a survival battel,fight fiercely")
                print_pause("Your sword is powerful "
                            f"kill the {enemy}")
                print_pause(" You are victorious!")
            else:
                print_pause("You did your best")
                print_pause("but your dagger is no match for the "
                            f"{enemy}")
                print_pause("You have been defeated!")
            play_again()
            break
        if choice2 == "2":
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been "
                        "followed.")
            field(item, enemy)
            break



def field(item, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            cave(item, option)
            break



def play_game():
    item = []
    enemy = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                            "gorgon"])
    introduction(item, enemy)
    field(item, enemy)


play_game()
