import random

def printBeginning():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)

def getSum(cards):
    sum = 0
    for i in cards:
        if i == 1 and sum + 11 <= 21:
            sum += 11
        else:
            sum += i
    return sum

def printResult(playerSum, compSum):
    if playerSum > compSum and playerSum <= 21:
        print("You Win")
    elif playerSum > compSum and playerSum > 21:
        print("You Lose")
    elif playerSum < compSum and compSum > 21:
        print("You Win")
    elif compSum > playerSum and compSum <= 21:
        print("You lose")
    else:
        print("Draw")

def dealCards(playersCards, computerCards, cards):
    firstPlayerCard = random.choice(cards)
    secondPlayerCard = random.choice(cards)
    firsCompCard = random.choice(cards)
    secondCompCard = random.choice(cards)
    playersCards.append(firstPlayerCard)
    playersCards.append(secondPlayerCard)
    computerCards.append(firsCompCard)
    computerCards.append(secondCompCard)

def dealMoreCards(computerCards, cards):
    while getSum(computerCards) < 17:
        card = random.choice(cards)
        computerCards.append(card)

def playBlackjack():
    yesOrNo = input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ")

    if yesOrNo == "y":
        printBeginning()
        bust = False
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        playersCards = []
        computerCards = []

        dealCards(playersCards, computerCards, cards)

        print(f"Your cards: {playersCards}")
        print(f"Computer's first card: {computerCards[0]}")

        toContinue = True
        while toContinue:
            anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")

            if anotherCard == 'y':
                anotherPlayerCard = random.choice(cards)
                playersCards.append(anotherPlayerCard)
                if getSum(playersCards) > 21:
                    bust = True
                    toContinue = False
            else:
                toContinue = False

            print(playersCards)


        if bust:
            print("You Lose")
        else:
            if getSum(computerCards) < 17:
                dealMoreCards(computerCards, cards)

            print(f"Your final hand: {playersCards}")
            print(f"Computer's final hand: {computerCards}")

            playerSum = getSum(playersCards)
            compSum = getSum(computerCards)
            printResult(playerSum, compSum)
        playBlackjack()
    else:
        return


playBlackjack()
