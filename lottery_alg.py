import random

lotteryNumbers = []
starsNum = []

for i in range (5):
    number = random.randint(1,50)
    while number in lotteryNumbers:
        number = random.randint(1,50)
    lotteryNumbers.append(number)

lotteryNumbers.sort()

for i in range (2):
    number = random.randint(1,12)
    while number in starsNum:
        number = random.randint(1,12)
    starsNum.append(number)

starsNum.sort()

print (">> Lucky Dip EuroMillion: ")
print (lotteryNumbers)
print ("Stars: ")
print (starsNum)