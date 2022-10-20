import random

valid_list = ["rock","paper","scissors"]

#function to validate input
def validate_input(input_player):
    if input_player in valid_list:
        return True
    else:
        return False

input_player = input("Lets play rock, papper and scissors, choose one: ")

print("Is the input valid?")
print(validate_input(input_player))

#function to create a computer move.
def cm_function():
    computer_move = random.choice(valid_list)
    return computer_move

cm_function()
computer_move = cm_function()

computer = 0
player = 0

def winner(input_player, computer_move):
    if input_player == "rock":
        if computer_move == "rock":
            return "it is a tie"
        elif computer_move == "paper":
            return "computer wins"
        elif computer_move == "scissors":
            return "player wins"

    elif input_player == "paper":
        if computer_move == "rock":
            return "paper wins"
        elif computer_move == "paper":
            return "it is a tie"
        elif computer_move == "scissors":
            return "computer wins"

    elif input_player == "scissors":
        if computer_move == "rock":
            return "computer wins"
        elif computer_move == "paper":
            return "player wins"
        elif computer_move == "scissors":
            return "It is a tie"

print(winner(input_player, computer_move))
print("computer: ", computer_move)
print("player: ", input_player)



#def play(computer_move, input_player):


#play(computer_move, input_player)
#print(play(computer_move, input_player))

