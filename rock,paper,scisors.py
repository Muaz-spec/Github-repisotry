import random

options = ('rock', 'paper', 'scisors')

Player_wins = 0
Computer_wins = 0


is_running = True

while is_running:

    player= None
    computer = random.choice(options)

    while player not in options:
        player = input("Choose a options:(rock, paper, scisors): ").lower()


    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")


    if player == 'rock' and computer == 'scisors':
        print("You win!")
        Player_wins += 1
    elif  player == 'paper' and computer == 'rock':
        print("You win!")
        Player_wins += 1
    elif  player == 'scisors' and computer == 'paper':
        print("You win!")
        Player_wins += 1
    elif  player == computer:
        print("It is a draw")
        wins = 0
    else:
        print("You lose!")
        Computer_wins += 1
            
    if not  input("Do you want ot play again? (Y/N): ").lower() == 'y':
       is_running = False

    
print(f"You won {Player_wins} times!")
print(f"Computer won {Computer_wins} times!")
print("Thanks! for playing ")