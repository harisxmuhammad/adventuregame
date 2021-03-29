import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(1)


def intro(item, option):
    print_pause("You find yourself stranded in the Year 2020 in New York city, filled "
                "with dead and sick people.\n")
    print_pause("Rumor has it that a " + option + " has been killing people "
                "here, and has been terrifying the whole world.\n")
    print_pause("In front of you is a totally new protective face mask.\n")
    print_pause("To your right is $10,000 .\n")
    print_pause("In your hand is a gun (but not very "
                "effective) as it has no bullets.\n")


def cash(item, option):
    if "sward" in item:
        print_pause("\nYou go to your right to pick up the cash.")
        print_pause("\nYou've never had so much cash in your hands ever in your life")
        print_pause("\nYou walk away with the money.\n")
    else:
        print_pause("\nYou walk towards the money.")
        print_pause("\nIt turns out to be the most amount cash you have seen.")
        print_pause("\nSuddenly something falls from the sky right in front of you "
                    "rock.")
        print_pause("\nYou have found the alien laser sword!")
        print_pause("\nYou discard your useless gun and take "
                    "the laser sword with you.")
        print_pause("\nYou walk away with the laser sword.\n")
        item.append("sward")
    valid_input(item, option)


def mask(item, option):
    print_pause("\nYou approach towards the mask to pick it up.")
    print_pause("\nYou are about to pick it up "
                "until 5 people with " + option + " show up.")
    print_pause("\nEep! This is the " + option + "' zone and you quickly pick the mask!")
    print_pause("\nThe people with " + option + " try to attack you!\n")
    if "sward" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a gun with no bullets.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) run away?")
        if choice2 == "1":
            if "sward" in item:
                print_pause("\nAs " + option + " people moves to attack, "
                            "you pull out laser sword, the perfect weapon!")
                print_pause("\nThe Sword of laser shines brightly in red "
                            "your hand glows up as you prepare yourself for the "
                            "attack.")
                print_pause("\nBut the people with " + option + "take one look at "
                            "your deadly laser sword and runs away!")
                print_pause("\nYou have saved yourself from getting the " + option +
                            ". You are victorious and negative!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your laser is no match for the people with"
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run away from the people with the cash1. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            valid_input(item, option)
            break


def valid_input(prompt, option):
    print_pause("Enter 1 to pick up the new protective mask.")
    print_pause("Enter 2 to take the $10,000.")
    print_pause("What would you like to do?")
    while True:
        option = input(prompt).lower()
        if option in option:
            return option


def ab():
    while True:
        choice1 = valid_input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            mask()
            break
        elif choice1 == "2":
            cash()
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nPerfect! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["Covid-19", "Virus", "Chinese Virus", "Corona"])
    intro(item, option)
    valid_input(item, option)


play_game()
