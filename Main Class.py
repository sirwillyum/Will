import random
import time
gold = 0
opphealth = 100
health = 100
strength = 10
dodge = 3
level = 1
chance = 3
print('press any key to start')
start = input()



chance = 0

def flip():
    global chance
    chance = random.randint(0, dodge)

def skeletonhit():
    global health
    health = health - 25
def wolfhit():
    global health
    health = health - 15
def golemhit():
    global health
    health = health - 25
def goblinhit():
    global health
    health = health - 15
def chomphit():
    global health
    health = health - 25
def pythonshit():
    global health
    health = health - 15
def spiderhit():
    global health
    health = health - 15
def attack():
    global opphealth
    opphealth = opphealth - strength
def giveGold():
    global gold
    gold = gold + 1
def addStrength():
    global strength
    strength = strength + 5
def addHealth():
    global health
    health = health + 5



skeletonstats = opphealth + 100
wolfstats = opphealth + 20
golemstats = opphealth + 100
goblinstats = opphealth + 20
chompstats = opphealth + 100
pythonstats = opphealth + 20
spiderstats = opphealth + 20


print("choose a character")
print("s: Shell", "Health:", health + 30, "Strength:", strength - 1, "Dodge:", dodge + 3)
print("t: Tank", "Health:", health, "Strength:", strength + 10, "Dodge:", dodge)
print("m: Mini", "Health:", health - 30, "Strength:", strength - 5, "Dodge:", dodge + 9)

character = input()
while character != 's' and character != 't' and character != 'm':
    print("choose a character")
    character = input()
if character == 's':
    print ('you have chosen ' + character + 'hell')
    health = health + 30
    strength = strength - 1
    dodge = dodge + 3
elif character == 't':
    print ('you have chosen ' + character + 'ank')
    strength = strength + 10
elif character == 'm':
    print ('you have chosen ' + character + 'ini')
    health = health - 30
    strength = strength - 5
    dodge = dodge + 9
print("choose a weapon s: sword sp: spoon k: knife m: mace")
weapon = input()
while weapon != 's' and weapon != 'sp' and weapon != 'k' and weapon != 'm':
    print("choose a weapon")
    weapon = input()
if weapon == 's':
    print ('you have chosen ' + weapon + 'word')
    strength = strength + 6
    if dodge > 4:
       dodge = dodge - 2
elif weapon == 'sp':
    strength = strength + 2
    print ('you have chosen ' + weapon + 'oon')
elif weapon == 'k':
    strength = strength + 3
    print ('you have chosen ' + weapon + 'nife')
elif weapon == 'm':
    print('you have chosen ' + weapon + 'ace')
    strength = strength + 5
    if dodge > 3:
        dodge = dodge - 1




print("Where do you want to go? c: cave d: desert f: forest")
land = input()
while land != 'c' and land != 'd' and land != 'f':
    land = input()
    print("Where do you want to go?")
if land == 'c':
    print("you've " "moved to the cave")
elif land == 'd':
    print("you've " "moved to the desert biome")
elif land == 'f':
    print("you've " "moved to the forest biome")

print("You will now fight an enemy")


if land == 'c' and level == 1:
    print("A spider has approached")
    print("Make a move, y or n?")
    choose = input()
    while health > 0 and opphealth > 0:
        print("enemy health is ", opphealth)
        print("Attack again? y or n")
        print("Gold:", gold)
        print("dodge ", dodge)
        choose = input()
        flip()
        if chance == 1 and choose == 'y':
            attack()
            giveGold()
            print("hit")
        elif chance == 2 and choose == 'y':
            spiderhit()
            print("hit was ineffective, you have", health, "Health Left")
        elif chance >= 2 and choose == 'y':
            addHealth()
            print("Enemy miss, you've healed to ", health, "Health")
        elif choose == 'n':
            print("You avoided the spider, but now you'll have to run somewhere else")
if opphealth < 1:
    print("You killed the spider")
    level = 2
elif health < 1:
    print("You Died")

if land == 'd' and level == 1:
    print("A python snake has approached you")
    print("Make a move, y or n?")
if land == 'f':
    print("A wolf has approached you")
    print("Make a move, y or n?")

print("You've made it to Level 2")

if land == 'c' and level == 2:
    print("A skeleton has approached you")
    print("Make a move, y or n?")
    if land == 'd':
        print("A golem has approached you")
        print("Make a move, y or n?")
    if land == 'f':
        print("A wild Chomp has appeared")
        print("Make a move, y or n?")
        while health > 0 and opphealth > 0:
            print("Attack again? y or n")
            print("Gold:", gold)
            choose = input()
            flip()
            if chance % 2 == 0 and choose == 'y':
                attack()
                giveGold()
            if chance % 2 == 1 and choose == 'y':
                spiderhit()
                print("hit was ineffective, you have", health, "Health Left")
            if choose == 'n':
                print("You avoided the chomp, looks like you'll have to ")
            if opphealth < 1:
                print("you killed the Chomp")
