import random
def fileReader(aFile):
    filename = open(aFile,"r")
    total = 0
    for line in filename:
        total = int(line)
    filename.close()   
    return total

def fileChanger(winnings,aFile):
    filename2 = open(aFile,"w")
    filename2.write(winnings)
    filename2.close()


def play():
    bet = int(input("What is your bet: $"))
    currentMoney = int(fileReader("betting.csv"))
    while bet > currentMoney:
        print("You don't have that much money to bet. Please enter an amount less than or equal to " + str(currentMoney))
        bet = int(input("What is your bet: $"))
    guess = input("What is your guess? ")
    currentMoney = int(fileReader("betting.csv"))
    randomNum = random.random()
    winningSide = ""
    if randomNum < .5:
        winningSide = "Heads"
    else:
        winningSide = "Tails"
    while guess != "Heads" and guess != "Tails":
        print("Not a valid guess. Must input either 'Heads' or 'Tails'")
        guess = input("What is your guess? ") 
    if guess == winningSide:
        fileChanger(str(currentMoney + bet),"betting.csv")
        return "You won $" + str(bet) + " with your guess of " + guess
    else:
        fileChanger(str(currentMoney - bet),"betting.csv")
        return "You lost $" + str(bet) + " with your guess of " + guess
print(play())
