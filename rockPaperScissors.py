import random, sys

print("ROCK, PAPER, SCISSORS")

# number of points
wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:
        print("Enter your move (r)ock, (p)aper, (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Type one of r, p, s, or q")

    # display player`s choose
    if playerMove == "r":
        print("ROCK versus...")
    if playerMove == "p":
        print("PAPER versus...")
    if playerMove == "s":
        print("SCISSORS versus...")

    # display computer`s choose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    if randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    if randomNumber == 1:
        computerMove = "s"
        print("SCISSORS")

