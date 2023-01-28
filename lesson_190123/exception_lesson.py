import random


def run_game():
    game_list = ["Rock", "Paper", "Scissor"]
    player1 = random.choice(game_list)
    player2 = random.choice(game_list)

    if player1 == "rock" and player2 == "paper":
        print("Player 2 Won")
    elif player1 == "paper" and player2 == "scissor":
        print("Player 2 Won")
    elif player1 == "scissor" and player2 == "rock":
        print("Player 2 Won")
    elif player1 == player2:
        print("Tie")
    else:
        print("Player 1 Won")


x = map(run_game, range(1, 10))
print(x)
print(list(x))
