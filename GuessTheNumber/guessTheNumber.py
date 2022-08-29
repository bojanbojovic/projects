import random

def printBeginning():
    logo = """
   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       
    """
    print(logo)

printBeginning()
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    numberOfAttempts = 10
else:
    numberOfAttempts = 5

while numberOfAttempts > 0:
    print(f"You have {numberOfAttempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess < number:
        print("Too low.")
        numberOfAttempts -= 1
    else:
        print("Too high.")
        numberOfAttempts -= 1

if numberOfAttempts == 0:
    print("You lose")
