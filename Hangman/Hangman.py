import random

def pickWord():
    f = open("/home/bojan/Downloads/Words.txt", 'r')
    str = f.read()
    words = str.split()
    word = random.choice(words)
    return word.lower()

def createDisplay(display, word):
    for i in word:
        display.append("_")

def updateDisplay(display, word, guess):
    j = 0
    for i in word:
        if i == guess:
            display[j] = i
        j += 1

def thereIsBlankSpaces(display):
    for i in display:
        if i =="_":
            return True
    return False

def createStages(stages):
    stages.append('''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''')
    stages.append('''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''')
    stages.append('''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''')

    stages.append('''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''')


    stages.append('''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''')
    stages.append('''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''')
    stages.append('''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''')

def guessIsWrong(guess,word):
    for i in word:
        if i == guess:
            return False
    return True

def guessRepettion(guess, display):
    for i in display:
        if guess == i:
            return True
    return False

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print (logo)
word = pickWord()
stages = []
createStages(stages)
display = []
createDisplay(display, word)
lives = 6

while thereIsBlankSpaces(display):
    guess = input("Guess a letter: ").lower()

    if guessIsWrong(guess, word):
        print(f"Letter {guess} is not in word.")
        lives -= 1
        print(stages[lives])
    elif guessRepettion(guess,display):
        print(f"Letter {guess} is already chosen.")

    if lives == 0:
        break

    updateDisplay(display, word, guess)
    print(' '.join(display))

if lives == 0:
    print(f"You lost. Word is {word}")
else:
    print("You win.")




