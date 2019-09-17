from banner import banner
import random
# 1 = rock
# 2 = paper
# 3 = scissors
def get_player_choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("What is your choice? "))
    return choice

def scoreboard(p_score,c_score):
    print(f"SCORE: Player {p_score} , Computer {c_score}")


banner("ROCK, PAPER, SCISSORS", "Allison.T")
welcome_banner = input("We are going to play Rock, Paper, Scissors. The first to win two out of of three rounds is the winner. !ENTER!")

cpu_score = 0
player_score = 0

while player_score < 2 and cpu_score < 2:
    scoreboard(player_score, cpu_score)
    player_choice = get_player_choice()
    cpu_choice = random.randint(1,3)
    if player_choice == 1:
        if cpu_choice == 1:
            print("TIE :-|")
        if cpu_choice == 2:
            print("LOSE :-(")
            cpu_score = cpu_score + 1
        if cpu_choice == 3:
            print("WIN :-)")
            player_score = player_score + 1
    if player_choice == 2:
        if cpu_choice == 1:
            print("WIN :-)")
            player_score = player_score + 1
        if cpu_choice == 2:
            print("TIE :-|")
        if cpu_choice == 3:
            print("LOSE :-(")
            cpu_score = cpu_score + 1
    if player_choice == 3:
        if cpu_choice == 1:
            print("LOSE :-(")
            cpu_score = cpu_score + 1
        if cpu_choice == 2:
            print("WIN :-)")
            player_score = player_score + 1
        if cpu_choice == 3:
            print("TIE :-|")
    if player_score == 2:
        print("YOU WIN , YOU STOP THE ROBOTS FROM TAKING OVER THE WORLD!!!")
    if cpu_score == 2:
        print("YOU LOSE, THE ROBOTS HAVE TAKING OVER THE WORLD!?!")