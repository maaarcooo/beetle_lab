# Beetle Lab
# Abandoned

import random

# Functions
def dise():
    return random.randint(1,6)

def num2name(number01):
    if number01 == 6:
        return "Body"
    elif number01 == 5:
        return "Head"
    elif number01 == 4:
        return "Tail"
    elif number01 == 3:
        return "Leg"
    elif number01 == 2:
        return "Antenna"
    elif number01 == 1:
        return "Eye"
    else:
        return "Not vaild"
        # For now

def vaild6(number):
    return number == 6



# Varibles
body01 = 0
head01 = 0
tail01 = 0
leg01 = 0
antenna01 = 0
eye01 = 0

win = False
# Target
# body01 = 1
# head01 = 1
# tail01 = 1
# leg01 = 4
# antenna01 = 2
# eye01 = 2

# Data structure
player01 = [0,0,0,0,0,0]

# Logic01
rand_dise = ""
while rand_dise != 6:
    rand_dise = dise()

    print(num2name(rand_dise))
    if rand_dise == 6:
        print("Test is 6")
    else:
        print(rand_dise)
        # break
        # For now

# Logic02
while not win:
    # print(f"{num2name(6)}: {body01}\n{num2name(5)}: {head01}\n{num2name(4)}: {tail01}\n{num2name(3)}: {leg01}\n{num2name(2)}: {antenna01}\n{num2name(1)}: {eye01}")
    print(f"{num2name(6)}: {body01}")
    print(f"{num2name(5)}: {head01}")
    print(f"{num2name(4)}: {tail01}")
    print(f"{num2name(3)}: {leg01}")
    print(f"{num2name(2)}: {antenna01}")
    print(f"{num2name(1)}: {eye01}")

    rand_dise = dise()
    print(f"Dise result: {rand_dise}/{num2name(rand_dise)}")
    while vaild6():
        print("")

    break
