import random


def red(text):
    print("\033[91m {}\033[00m" .format(text))


def cyan(text):
    print("\033[96m {}\033[00m" .format(text))


def yellow(text):
    print("\033[93m {}\033[00m" .format(text))


def green(text):
    print("\033[92m {}\033[00m" .format(text))


def purple(text):
    print("\033[95m {}\033[00m" .format(text))


win_counter = 0
draw_counter = 0
loss_counter = 0
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
while True:
    player_move = input("Choose rock, paper or scissors by typing the first letter of your choice: (r/p/s)")
    if player_move.lower() == "r":
        player_move = rock
    elif player_move.lower() == "s":
        player_move = scissors
    elif player_move.lower() == "p":
        player_move = paper
    else:
        print("Invalid input!")
        continue
    cyan(f"You chose {player_move}!")
    computer_choice = random.randint(1, 3)
    computer_move = ""
    if computer_choice == 1:
        computer_move = rock
    elif computer_choice == 2:
        computer_move = scissors
    else:  # computer_choice == 3
        computer_move = paper
    cyan(f"The computer chose {computer_move}!")
    if (player_move == rock and computer_move == scissors) or \
            (player_move == scissors and computer_move == paper) or \
            (player_move == paper and computer_move == rock):
        green("You win!")
        win_counter += 1
    elif player_move == computer_move:
        yellow("Draw!")
        draw_counter += 1
    else:  # the options for being defeated by the computer
        red("You lose!")
        loss_counter += 1
    purple(f'''Current stats:
             Games won: {win_counter}
             Games lost: {loss_counter}
             Draws: {draw_counter}''')
    play_again_or_quit = input("Would you like to play again? (y/n)")
    if play_again_or_quit.lower() == "y":
        continue
    elif play_again_or_quit.lower() == "n":
        green("Thank you for playing!")
        break
    else:
        raise SystemExit(red('Invalid input, exiting game!'))
