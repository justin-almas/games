import random
import math
def randomCard():  #get card when player or dealer hits+
    cards = ["A","K","J","Q","10","9","8","7","6","5","4","3","2"]
    number = random.randint(0,len(cards)-1)
    try:
        return cards[number]
    except:
        return "A"
# ideas for dealer play. Have lists of their cards and update totals. Have them both go until they bust or stay. need dealer program but can get that from assignment.
# no options for splits or no betting system. Potentially implement later if you want.

def dealer(card):
    a_is_11 = 0
    a_is_1 = 0
    for char in card:  # i think this still works with lists instead of strings
        if char == "A":
            a_is_1 += 1
            a_is_11 += 11
        elif char == "K" or char == "J" or char == "Q":
            a_is_1 += 10
            a_is_11 += 10
        else:
            a_is_1 += int(char)
            a_is_11 += int(char)

    if a_is_11 >= 17 and a_is_11 <= 21:
        return "Stay"
    elif a_is_1 >= 17 and a_is_1 <= 21:
        return "Stay"
    elif a_is_1 < 17:
        return "Hit"
    else:
        return "Bust"
def listTotal(aList):
    a11 = 0
    a1 = 0
    for element in aList:
        if element == "A":
            a11 += 11
            a1 += 1
        elif element == "K" or element == "Q" or element == "J":
            a11 += 10
            a1 += 10
        else:
            a11 += int(element)
            a1 += int(element)
    return [a11,a1]

def play():
    listPlayer = []
    listDealer = []
    listDealer.append(randomCard())
    listDealer.append(randomCard())
    listPlayer.append(randomCard())
    listPlayer.append(randomCard())
    while listTotal(listPlayer)[0] != 21 and listTotal(listPlayer)[1] != 21 and listTotal(listPlayer)[1] < 21:
        print(listPlayer)
        move = input("What is your move? ")
        while move != "Hit" and move != "Stay":
            print("Not a valid move. Must input either 'Hit' or 'Stay'")
            move = input("What is your move? ")
        if move == "Hit":
            listPlayer.append(randomCard())
        elif move == "Stay":
            break    # may need to work on this line
    if listTotal(listPlayer)[0] == 21 or listTotal(listPlayer)[1] == 21:
        return "Blackjack! You won! " + ",".join(listDealer) + " " + ",".join(listPlayer)
    elif listTotal(listPlayer)[0] > 21 and listTotal(listPlayer)[1] > 21:
        return "Bust. Dealer won. " + ",".join(listDealer) + " " + ",".join(listPlayer)
    else:
        while listTotal(listDealer)[0] != 21 and listTotal(listDealer)[1] != 21 and (listTotal(listDealer)[0] < 21 or listTotal(listDealer)[1] < 21) and  listTotal(listDealer)[0] < listTotal(listPlayer)[0] and listTotal(listDealer)[1] < listTotal(listPlayer)[1]:
            moveDealer = dealer(listDealer)
            if moveDealer == "Hit":
                print("Dealer Hit")
                listDealer.append(randomCard())
            elif moveDealer == "Stay":
                print("Dealer Stay")
                break
        #compare score
    dealerAHigh = listTotal(listDealer)[0]
    dealerALow = listTotal(listDealer)[1]
    playerAHigh = listTotal(listPlayer)[0]
    playerALow = listTotal(listPlayer)[1]
    if dealerAHigh == 21 or dealerALow == 21:
        return "You lose. Dealer got blackjack. " + ",".join(listDealer) + " " + ",".join(listPlayer)
    elif dealerAHigh > 21 and dealerALow > 21:
        return "You win! Dealer busted. " + ",".join(listDealer) + " " + ",".join(listPlayer)
    elif (dealerAHigh > playerAHigh or dealerAHigh > playerALow) and dealerAHigh <= 21: #still probably buggy
        return "You lose. Dealer beat your score. " + ",".join(listDealer) + " " + ",".join(listPlayer)
    elif (dealerALow > playerALow or dealerALow > playerAHigh) and dealerALow <= 21:
        return "You lose. Dealer beat your score. " + ",".join(listDealer) + " " + ",".join(listPlayer)
    elif dealerAHigh == playerAHigh and dealerAHigh <= 21:
        return "It's a tie. " + ",".join(listDealer) + " " + ",".join(listPlayer)
    elif dealerALow == playerALow and dealerALow <= 21:
        return "It's a tie. " + ",".join(listDealer) + " " + ",".join(listPlayer)
    else:
        return "You won! You beat the dealer's score! " + ",".join(listDealer) + " " + ",".join(listPlayer)
    #find way to play unlimited times till bust
print(play())

