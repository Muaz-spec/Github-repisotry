import random
    
lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number, highest_number)

guesses = 0

print("Wlecome to python random number guessing game!")
print(f"Choose a number between {lowest_number} and {highest_number}")

is_running = True
while is_running:

    guess = input("Enter a number: ")

    if guess.isdigit():
        guess = int(guess)
        
        if guess <lowest_number or guess > highest_number:
            print("That number is out of range!")
            print(f"Choose a number between {lowest_number} and {highest_number}: ")
        elif guess > answer:
            print("Your guess is too high!")
            print("Guess a lower number")
            guesses += 1
        elif guess < answer:
            print("Your guess is too low!")
            print("Guess a higher number")
            guesses += 1
        elif guess == answer:
            print("***************")
            print("CORRECT!!!")
            print("***************")
            print(f"The correct answer was {answer}")

            if not input("Play again? (Y/N): ").lower() == "y":
                is_running = False

    else:
        print("Invalid Guess!")
        print(f"Choose a number between {lowest_number} and {highest_number}: ")


print(f"You guessed it in {guesses} guesses")
print("Thanks for playing!")  