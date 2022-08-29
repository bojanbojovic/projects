import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

playerChoose = int(input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
compChoose = random.randint(0,2)

if playerChoose == 0 and compChoose == 0:
    print(rock)
    print("Computer choose:\n" + rock)
    print("Even.")
elif playerChoose == 0 and compChoose == 1:
    print(rock)
    print("Computer choose:\n" + paper)
    print("You lose.")
elif playerChoose == 0 and compChoose == 2:
    print(rock)
    print("Computer choose:\n" + scissors)
    print("You win.")
elif playerChoose == 1 and compChoose == 0:
    print(paper)
    print("Computer choose:\n" + rock)
    print("You win.")
elif playerChoose == 1 and compChoose == 1:
    print(paper)
    print("Computer choose:\n" + paper)
    print("Even.")
elif playerChoose == 1 and compChoose == 2:
    print(paper)
    print("Computer choose:\n" + scissors)
    print("You lose.")
elif playerChoose == 2 and compChoose == 0:
    print(scissors)
    print("Computer choose:\n" + rock)
    print("You lose.")
elif playerChoose == 2 and compChoose == 1:
    print(scissors)
    print("Computer choose:\n" + paper)
    print("You win.")
elif playerChoose == 2 and compChoose == 2:
    print(scissors)
    print("Computer choose:\n" + scissors)
    print("Even.")


