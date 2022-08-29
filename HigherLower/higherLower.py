import random
import json


def printLogo():
    logo = """
        __  ___       __             
       / / / (_)___ _/ /_  ___  _____
      / /_/ / / __ `/ __ \/ _ \/ ___/
     / __  / / /_/ / / / /  __/ /    
    /_/ ///_/\__, /_/ /_/\___/_/     
       / /  /____/_      _____  _____
      / /   / __ \ | /| / / _ \/ ___/
     / /___/ /_/ / |/ |/ /  __/ /    
    /_____/\____/|__/|__/\___/_/     
    """
    print(logo)

def printVs():
    vs = """
     _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)
    """
    print(vs)

def getWinner(first, second, whoHasMore):
    if first.get('follower_count') > second.get('follower_count') and whoHasMore == 'A':
        return True
    elif first.get('follower_count') < second.get('follower_count') and whoHasMore == 'A':
        return False
    elif first.get('follower_count') > second.get('follower_count') and whoHasMore == 'B':
        return False
    else:
        return True

def playGame():
    with open(file="data.json") as file:
        data = json.load(file)
    score = 0
    answer = False
    isWinning = True
    printLogo()
    while isWinning:
        if not answer:
            first = random.choice(data)
        print(f"Compare A: {first.get('name')}, a {first.get('description')}, from {first.get('country')}.")
        printVs()
        second = random.choice(data)
        while first == second:
            second = random.choice(data)
        print(f"Compare B: {second.get('name')}, a {second.get('description')}, from {second.get('country')}.")
        whoHasMore = input("Who has more followers ? Type 'A' or 'B': ")
        answer = getWinner(first, second, whoHasMore)

        if answer:
            score += 1
            printLogo()
            print(f"You're right! Current score: {score}.")
            first = second
            answer = True
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            isWinning = False


playGame()

