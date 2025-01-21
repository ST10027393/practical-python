# bounce.py
#
# Exercise 1.5
ballHeight = 100
heighLoss = 0.6
bounces = 10
i = 0

while i < bounces:
    ballHeight = ballHeight * heighLoss
    print(i + 1, round(ballHeight, 4))
    i += 1