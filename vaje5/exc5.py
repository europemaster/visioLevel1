from random import random

# Instructions

# Create a program that represents a football bet.
# The program needs to have a list of football matches, where for every match user should input
# the end result. There needs to be at least 5 matches. Example of input:
# (programs output) Liverpool : CSKA ?
# (user's input) 1-0
# (programs output) Bate Borisov : Partizan  ?
#  ....

# After user inputs all the results, program waits for 10 seconds and prints the result of matches.
# Results are totally random, you can say that max. goals by one team is 5.
# After results are displayed, program should output, how well were the bets.
# For every correctly guessed match, user gets 10€, for every incorrect user loses 1€
# Example of output:
# Actual game: Liverpool : CSKA 3-0.
# Your bet: 1-0
# You lose 1€
# ....
# --------------
# You earned -5€.


list_home = ["Liverpool", "Bate Borisov", "Olimpija", "Milan", "Barcelona"]
list_away = ["CSKA", "Partizan", "Juventus", "Bayern", "PSV"]
user_results = []


def bet():
    print("Input your forecast, maximum goal by one team is 5")
    for i, v in enumerate(list_home):
        success = False
        while not success:
            inp = input("{} : {} ?\n".format(v, list_away[i]))
            if len(inp) < 3:
                print("Invalid input")
            else:
                user_results.append(inp)
                success = True


def match_generator():
    return str(int(random() * 5) + 1), str(int(random() * 5) + 1)


bet()
earnings = 0
print("\t\t[Bet results]...")
for ind, v in enumerate(user_results):
    home, away = match_generator()
    print("Actual game result:\n {} {} : {} {}".format(list_home[ind], home, away, list_away[ind]))
    if v[0] == home and away in v[0:]:
        print("BRAVO, YOU EARNED 10€ !!!")
        earnings += 10
    else:
        print("Your bet:\n {} {} : {} {}".format(list_home[ind], v[0], v[2], list_away[ind]) + "\n---------------------")
        earnings -= 1
print("Money earned: {}€".format(earnings))

