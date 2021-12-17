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
        if move == "Hit":
            listPlayer.append(randomCard())
        elif move == "Stay":
            break    # may need to work on this line
    if listTotal(listPlayer)[0] == 21 or listTotal(listPlayer)[1] == 21:
        return "Blackjack! You won!" + "".join(listDealer) + " " + "".join(listPlayer)
    elif listTotal(listPlayer)[0] > 21 and listTotal(listPlayer)[1] > 21:
        return "Bust. Dealer won." + "".join(listDealer) + " " + "".join(listPlayer)
    else:
        while listTotal(listDealer)[0] != 21 and listTotal(listDealer)[1] != 21 and (listTotal(listDealer)[0] < 21 or listTotal(listDealer)[1] < 21) and  listTotal(listDealer)[0] < listTotal(listPlayer)[0] and listTotal(listDealer)[1] < listTotal(listPlayer)[1]:
            moveDealer = dealer(listDealer)
            if moveDealer == "Hit":
                print("Dealer Hit")
                listDealer.append(randomCard())
            elif moveDealer == "Stay":
                print("Dealer Stay")
                break
            else:
                return "Dealer busted! You won!" + "".join(listDealer) + " " + "".join(listPlayer)
        #compare scores
    if listTotal(listDealer)[0] == 21 or listTotal(listDealer)[1] == 21:
        return "Dealer got blackjack. You lose." + "".join(listDealer) + " " + "".join(listPlayer)
    elif listTotal(listDealer)[0] >= 21 and listTotal(listDealer)[1] >= 21:
        return "Dealer busted. You win!" + "".join(listDealer) + " " + "".join(listPlayer)
    elif listTotal(listDealer)[0] > listTotal(listPlayer)[0] or (listTotal(listDealer)[1] > listTotal(listPlayer)[1] and listTotal(listDealer)[1] <= 21):
        return "Dealer beat your score. You lose." + "".join(listDealer) + " " + "".join(listPlayer)
    elif listTotal(listDealer)[0] == listTotal(listPlayer)[0] or listTotal(listDealer)[1] == listTotal(listPlayer)[1]:
        return "It's a tie. Nobody wins." + "".join(listDealer) + " " + "".join(listPlayer)
    else:
        return "You beat the dealer's score! You win!" + "".join(listDealer) + " " + "".join(listPlayer)
    #find way to play unlimited times till bust
print(play())

