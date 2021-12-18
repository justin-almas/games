import random
def fileReader():
    filename = open("betting.csv","r")
    total = 0
    for line in filename:
        total = int(line)
    filename.close()   
    return total

def fileChanger(winnings):
    filename2 = open("betting.csv","w")
    filename2.write(winnings)
    filename2.close()


def play():
    bet = int(input("What is your bet: $"))
    guess = input("What is your guess? ")
    currentMoney = int(fileReader())
    randomNum = random.random()
    winningSide = ""
    if randomNum < .5:
        winningSide = "Heads"
    else:
        winningSide = "Tails"
    if guess == winningSide:
        fileChanger(str(currentMoney + bet))
        return "You won $" + str(bet) + " with your guess of " + guess
    else:
        fileChanger(str(currentMoney - bet))
        return "You lost $" + str(bet) + " with your guess of " + guess
print(play())
