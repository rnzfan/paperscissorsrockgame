#! usr/bin/env python
"""This is a fun "Paper, Scissors, Rock" Game"""

import random

userinput = {"P": "Paper", "S": "Scissors", "R": "Rock"}
computerinput = {0: "Paper", 1: "Scissors", 2: "Rock"}
userkey = "initial"
computerscore = 0
userscore = 0

print("Welcome to the \"Paper, Scissors, Rock\" Game\n")

while userkey != "E":    
    userkey = input("What is your choice?\n"
                        "[P] for Paper\n"
                        "[S] for Scissors\n"
                        "[R] for Rock\n"
                        "[E] for exit\n")
    if userkey == "E":
        print(f"Your score is {userscore}")
        print(f"Computer score is {computerscore}")
        continue
    elif (userkey != "P") & (userkey != "S") & (userkey != "R"):
        print("Your input is invalid, please input again!\n")
        continue

    print(f"Your choice is {userinput[userkey]}")
    computerkey = random.randint(0,2)
    print(f"The computer choice is {computerinput[computerkey]}")
    if userinput[userkey] == computerinput[computerkey]:
        print("This is a tie\n")
    if ((userinput[userkey] == "Paper") & (computerinput[computerkey] == "Rock")) | \
        ((userinput[userkey] == "Rock") & (computerinput[computerkey] == "Scissors")) | \
        ((userinput[userkey] == "Scissors") & (computerinput[computerkey] == "Paper")):
        print("You are the Winner!\n")
        userscore = userscore + 1
    if ((userinput[userkey] == "Paper") & (computerinput[computerkey] == "Scissors")) | \
        ((userinput[userkey] == "Rock") & (computerinput[computerkey] == "Paper")) | \
        ((userinput[userkey] == "Scissors") & (computerinput[computerkey] == "Rock")):
        print("Oh, you lose!\n")
        computerscore = computerscore + 1
