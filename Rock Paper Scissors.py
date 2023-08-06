import random


#function for continuing game loop if player wants to
def restart():
    again = input("Play Again? y for YES, n for NO - ").lower()
    #calling the game loop if player wants to
    if again == "y":
        game_loop()
    #quiting the game if player wants to
    elif again == "n":
        print("Game Quit.")
    else:
        print("Quitting.")


#function containing the main game logic
def game_loop():
    cpu_choices = ["Rock", "Paper", "Scissors"]
    player_choices = ["Rock", "Paper", "Scissors"]
    choice = random.randrange(0, 3) #creating random numbers for CPU to choose its move
    cpu_choice = cpu_choices[choice] #picking CPU move
    player_choice = input("Enter r for rock, p for papers or s for scissors: ").lower()

    #conditions for when player chooses Rock
    if player_choice == 'r':
        player_choice = player_choices[0]
        print("You: {}".format(player_choice)) #displaying player move
        print("CPU: {}".format(cpu_choice)) #displaying CPU move
        if player_choice == cpu_choice:
            print("Draw.")
        if player_choice == "Rock" and cpu_choice == "Paper":
            print("CPU wins.")
        if player_choice == "Rock" and cpu_choice == "Scissors":
            print("You win.")

    #conditions for when player chooses Paper
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

    #conditions for when player chooses Scissors
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

    #condition for when player chooses incorrect move
    else:
        print('Invalid move.')

    restart()


#starting the game loop
game_loop()
