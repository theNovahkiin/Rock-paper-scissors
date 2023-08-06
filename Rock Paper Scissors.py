import random


def restart():
    again = input("Play Again? y for YES, n for NO - ").lower()
    if again == "y":
        game_loop()
    elif again == "n":
        print("Game Quit.")
    else:
        print("Quitting.")


def game_loop():
    cpu_choices = ["Rock", "Paper", "Scissors"]
    player_choices = ["Rock", "Paper", "Scissors"]
    choice = random.randrange(0, 3)
    cpu_choice = cpu_choices[choice]
    player_choice = input("Enter r for rock, p for papers or s for scissors: ").lower()
    if player_choice == 'r':
        player_choice = player_choices[0]
        print("You: {}".format(player_choice))
        print("CPU: {}".format(cpu_choice))
        if player_choice == cpu_choice:
            print("Draw.")
        if player_choice == "Rock" and cpu_choice == "Paper":
            print("CPU wins.")
        if player_choice == "Rock" and cpu_choice == "Scissors":
            print("You win.")
    elif player_choice == 'p':
        player_choice = player_choices[1]
        print("You: {}".format(player_choice))
        print("CPU: {}".format(cpu_choice))
        if player_choice == cpu_choice:
            print("Draw.")
        if player_choice == "Paper" and cpu_choice == "Rock":
            print("You win.")
        if player_choice == "Paper" and cpu_choice == "Scissors":
            print("CPU wins.")
    elif player_choice == 's':
        player_choice = player_choices[2]
        print("You: {}".format(player_choice))
        print("CPU: {}".format(cpu_choice))
        if player_choice == cpu_choice:
            print("Draw.")
        if player_choice == "Scissors" and cpu_choice == "Paper":
            print("You win.")
        if player_choice == "Scissors" and cpu_choice == "Rock":
            print("CPU wins.")
    else:
        print('Invalid move.')
    restart()


game_loop()
