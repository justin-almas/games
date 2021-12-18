import random
def fileReader():
    filename = open("betting.csv","r")
    total = 0
    for line in filename:
        total = int(line)
    filename.close()   
    print(total)

def fileChanger():
    filename2 = open("betting.csv","w")
    filename2.write("10000")
    filename2.close()

def randomCard():  #get card when player or dealer hits+
    cards = ["1","0","9","8","7","6","5","4","3","2"] # do we adjust first or later ??????
    number = random.randint(0,len(cards)-1)
    try:
        return cards[number]
    except:
        return "1"
def sumAdjuster(twoNum):
    sum = 0
    for num in twoNum:
        sum += num
    if sum >= 10:
        sum -= 10
    return sum
def play():
    return 0
