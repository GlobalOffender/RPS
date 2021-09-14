import random
print("You're on the outskirts of Draggenhof, running allong the trade route that connects the kingdom to Usveein. You're being chased.")
print("The route leads through the shadowgreen caves, which is known for being a underground forest with alot of cravesses.")
print("Thus, there are alot of bridges. Some not so well kept. You're met with a rope bridge. It looked battle-scarred.")
steps = input("You approach the bridge, how many steps do you take? ")
if int(steps) <= 6:
    print(" ")
    print("As you walk across, the boards near the end of the bridge get loose and fall off into the cravess.")
    print("You back away. As you look around, you see a trader's carrage holding planks.")
    planks = input("You decide to grab some planks from there, but how many do you take? ")
    if int(planks) >= 8:
        print(" ")
        print("You grab " + str(planks) + " planks and place them where the old planks were. You get across!")
        print("You kick off the planks you placed once on the otherside and left the excess planks allong the path.")
        print("The guards chasing you get to the bridge. The owner of the carrage returns and yells at the guards, thinking they took his planks.")
    else:
        print(" ")
        print("You grab " + str(planks) + " planks and begin placing them. You don't have enough! The guards caught up and you ended up getting caught.")
        exit()
else:
    print(" ")
    print("As you walk across, the boards underneath you give out and you pummel into the cravess.")
    exit()
# Challenged
print(" ")
print("You get away, but a knight and his henchman challenge you to a match of RPS.")
print("Though, the knight doesn't want to fight you if you can't beat the henchman. Do you accept the challenge?")
answer = input("[Y/N] ").lower()
# RPS
if answer == "y":
    number = random.randint(1, 3)
    if number == 1:
        inputA1 = input("The henchman approaches! Rock, Paper, Scissors! ").lower()
        if inputA1 == "rock":
            numberA = random.randint(1, 3)
            if numberA == 1:
                inputAA1 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAA1 == "rock":
                    print("You've beaten the knight!")
                else:
                    print("You've lost against the knight.")
            if numberA == 2:
                inputAA2 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAA2 == "paper":
                    print("You've beaten the knight!")
                else:
                     print("You've lost against the knight.")
            if numberA == 3:
                inputAA3 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAA3 == "scissors":
                    print("You've beaten the knight!")
                else:
                    print("You've lost against the knight.")
        else:
            print("You've lost against the henchman.")
    if number == 2:
        inputA2 = input("The henchman approaches! Rock, Paper, Scissors! ").lower()
        if inputA2 == "paper":
            numberB = random.randint(1, 3)
            if numberB == 1:
                inputAB1 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAB1 == "rock":
                    print("You've beaten the knight!")
                else:
                    print("You've lost to the knight.")
            if numberB == 2:
                inputAB2 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAB2 == "paper":
                    print("You've beaten the knight!")
                else:
                    print("You've lost to the knight.")
            if numberB == 3:
                inputAB3 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAB3 == "scissors":
                    print("You've beaten the knight!")
                else:
                    print("You've lost to the knight.")
        else:
            print("You've lost against the henchman.")
    if number == 3:
        inputA3 = input("The henchman approaches! Rock, Paper, Scissors! ").lower()
        if inputA3 == "scissors":
            numberC = random.randint(1, 3)
            if numberC == 1:
                inputAC1 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAC1 == "rock":
                    print("You've beaten the knight!")
                else:
                    print("You've lost against the knight.")
            if numberC == 2:
                inputAC2 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAC2 == "paper":
                    print("You've beaten the knight!")
                else:
                    print("You've lost against the knight.")
            if numberC == 3:
                inputAC3 = input("You've beaten the henchman! Now it's the knight's turn. Rock, Paper, Scissors! ").lower()
                if inputAC3 == "scissors":
                    print("You've beaten the knight!")
                else:
                    print("You've lost against the knight.")
        else:
            print("You've lost against the henchman.")
else:
    print("You've denied the challenge.")