#! /bin/python3

import random

health = 50
difficulty = 1

potion_health = int(random.randint(25,50)/difficulty)
health = health + potion_health
print("Health of the player after taking potion is: {}".format(health))
