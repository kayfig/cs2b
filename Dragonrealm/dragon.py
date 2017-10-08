# Dragon Realm
# A game by Kamryn Figuerres
# Oct 8, 2017

import random
import time

def showIntroduction():
    print('''You are in a land full of dragons.
In front of you, you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, he will eat you on site.''')
    print()

def pickCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? 1 or 2")
        cave = input()
    return cave

showIntroduction()
pickCave()
