import os

def findAndPrintWinner(bids):
    highestBidName = next(iter(bids))
    highestBid = list(bids.values())[0]

    for key in bids:
        if bids[key] > highestBid:
            highestBid = bids[key]
            highestBidName = key

    print(f"The winner is {highestBidName} with a bid of ${highestBid}")

def printBeginning():
    logo = '''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''
    print(logo)

printBeginning()
print("Welcome to the secret auction program.")
bids = {}
isThereMoreBids = True

while isThereMoreBids:
    name = input("What is your name: ")
    bid = input("What's your bid:$ ")
    bids[name] = bid
    toContinue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if toContinue == "no":
        isThereMoreBids = False
    os.system('clear')

findAndPrintWinner(bids)
