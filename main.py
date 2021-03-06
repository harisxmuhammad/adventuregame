import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(1)


def play_game():
    option = random.choice(["Covid", "Virus"])
    intro(option)
    date(option)
    emily(option)
    scarlet_catfish()
    decision()


def valid_input(prompt, option):
    while True:
        choice = input(prompt).lower()
        if choice in option:
            return choice


def date(option):
    while True:
        choice1 = valid_input("(Please enter 1 or 2.)\n", ["1", "2"])
        if choice1 == "1":
            emily(option)
            break
        elif choice1 == "2":
            scarlet_catfish()


def decision():
    while True:
        choice2 = valid_input("(Please enter 1 to call the cops"
                              "or 2 to eat with the fat guy.)\n", ["1", "2"])
        if choice2 == "1":
            print_pause("\nYou called the cops and they come\n"
                        "You explain to them that this man is a fraud"
                        "and should be cut off from the internet")
        elif choice2 == "2":
            print_pause("You have lunch with the fat guy and try to understand"
                        "and try to understand why he is doing this")
            play_again()


def intro(option):
    print_pause("\nIt is " + option + " season and life is very boring.\n"
                "So Rafa downloaded Tinder"
                "\nHe has matched with girls due to his looks and charm\n")
    print_pause("However, he really likes talking to Scarlet and Emily\n"
                "\nSo he is indecisive, whom he should meet"
                "So should he go meet Scarlet or Emily")
    print_pause("Press 1 to meet Emily")
    print_pause("Press 2 to meet Scarlet")
    print_pause("\nPick a girl for your tinder date")


def emily(option):
    print_pause("\nYou guys have decided to meet for dinner"
                "at an Asian restaurant at 2pm\n"
                "You want to impress her, so you dress nice")
    print_pause("\nYou arrived 5 minutes late and you see her sitting\n"
                "In your brain, you are like damn! She is beautiful.\n"
                "\nHe goes to her and they hug and stuff\n"
                "They end up talking for hours and seem to be enjoying.")
    date(option)


def scarlet_catfish():
    print_pause("\nHe goes to the mall to meet Scarlet\n"
                "He arrived early, so he went to find a place to sit down\n"
                "\nThe girl texts him and says she is 5 minutes away"
                "So he waits")
    print_pause("\n10 minutes later, someone touched him"
                "on the shoulder from behind\n"
                "and it turned out to be a fat guy\n")
    print_pause("The fat guy says he is here to meet Rafa\n")
    decision()


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nPerfect! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


play_game()
