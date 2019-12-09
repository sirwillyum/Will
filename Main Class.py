import random
gold = 20
QnA = 3
opphealth = 100
health = 100
strength = 10
dodge = 3
level = 1
chance = 3
print('press any key to start')
start = input()
print('choose a difficulty')
print('h: hard')
print('m: medium')
print('e: easy')
difficulty = input()
while difficulty != 'h' and difficulty != 'm' and difficulty != 'e':
    difficulty = input()
    print("make a selection")
    if difficulty == 'h':
        opphealth = opphealth + 100
    if difficulty == 'm':
        opphealth = opphealth + 50
    if difficulty == 'e':
        opphealth = 100
chance = 0

def flip():
    global chance
    chance = random.randint(0, dodge)

def skeletonhit():
    global health
    health = health - 20
def wolfhit():
    global health
    health = health - 15
def golemhit():
    global health
    health = health - 20
def goblinhit():
    global health
    health = health - 15
def chomphit():
    global health
    health = health - 20
def pythonshit():
    global health
    health = health - 15
def spiderhit():
    global health
    health = health - 15
def knighthit():
    global health
    health = health - 25
def ogrehit():
    global health
    health = health - 25
def griffinhit():
    global health
    health = health - 25
def blackknighthit():
    global health
    health = health - 50
def attack():
    global opphealth
    opphealth = opphealth - strength
def giveGold():
    global gold
    gold = gold + 1
def addStrength():
    global strength
    strength = strength + 2
def addStrength2():
    global strength
    strength = strength + 5
def addStrength3():
    global strength
    strength = strength + 10
def upgrade_strength():
    global shop
    global gold
    global strength
    print("Would you like to upgrade your strength? press u, otherwise keep fighting. (Cost: 4 Gold) ")
    shop = input()
    print("select an option")
    if shop == 'u' and gold > 3:
        gold = gold - 4
        addStrength()
        print("Success! You've given yourself +2 Strength, you now have", strength, " Strength")
    elif shop == 'u' and gold < 4:
        print("insufficient funds. Play more to recieve more gold.")
def upgrade_strength2():
    global shop
    global gold
    global strength
    print("Would you like to upgrade your strength? press u, otherwise keep fighting. (Cost: 4 Gold) ")
    shop = input()
    print("select an option")
    if shop == 'u' and gold > 3:
        gold = gold - 4
        addStrength2()
        print("Success! You've given yourself +5 Strength, you now have", strength, " Strength")
    elif shop == 'u' and gold < 4:
        print("insufficient funds. Play more to recieve more gold.")
def upgrade_strength3():
    global shop
    global gold
    global strength
    print("Would you like to upgrade your strength? press u, otherwise keep fighting. (Cost: 4 Gold) ")
    shop = input()
    print("select an option")
    if shop == 'u' and gold > 3:
        gold = gold - 4
        addStrength3()
        print("Success! You've given yourself +5 Strength, you now have", strength, " Strength")
    elif shop == 'u' and gold < 4:
        print("insufficient funds. Play more to recieve more gold.")
def addHealth():
    global health
    health = health + 5
def addmoreHealth():
    global health
    health = health + 25
def print_stats():
    global opphealth
    global gold
    print("enemy health is ", opphealth)
    print("Gold:", gold)
    print("Attack again? y or n")
def level_2_stats():
    global opphealth
    opphealth = opphealth + 20
def level_3_stats():
    global opphealth
    opphealth = opphealth + 35
def level_BK_stats():
    global opphealth
    opphealth = opphealth + 50



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
print(gold, " Gold")
print("choose a weapon")
print("s: sword (16 Gold)")
print("sp: spoon (9 Gold)")
print("k: knife (11 Gold)")
print("m: mace (13 Gold)")
weapon = input()
while weapon != 's' and weapon != 'sp' and weapon != 'k' and weapon != 'm':
    print("choose a weapon")
    weapon = input()
if weapon == 's':
    print ('you have chosen ' + weapon + 'word')
    gold = gold - 16
    strength = strength + 6
    if dodge > 4:
           dodge = dodge - 2
elif weapon == 'sp':
    gold = gold - 9
    strength = strength + 2
    print ('you have chosen ' + weapon + 'oon')
elif weapon == 'k':
    gold = gold - 11
    strength = strength + 3
    print ('you have chosen ' + weapon + 'nife')
elif weapon == 'm':
    print('you have chosen ' + weapon + 'ace')
    gold = gold - 13
    strength = strength + 5
    if dodge > 3:
        dodge = dodge - 1



print(gold, " Gold")
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
    print("Make a move. press y to fight")
    choose = input()
    while health > 0 and opphealth > 0:
        print_stats()
        if gold > 4:
            upgrade_strength()

        choose = input()
        flip()
        if chance == 0 and choose == 'y':
            attack()
            giveGold()
            print("hit")
        elif chance == 1 and choose == 'y':
            spiderhit()
            print("hit was ineffective, you have", health, "Health Left")
        elif chance >= 2 and choose == 'y':
            addHealth()
            print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land == 'c':
    print("You killed the spider")
    level = 2
elif health < 1:
    print("You Died")

if land == 'd' and level == 1:
    print("A python snake has approached you")
    print("Make a move press y to fight")
    choose = input()
    while health > 0 and opphealth > 0:
        print_stats()
        if gold > 4:
            upgrade_strength()
        choose = input()
        flip()
        if chance == 0 and choose == 'y':
            attack()
            giveGold()
            print("hit")
        elif chance == 1 and choose == 'y':
            pythonshit()
            print("hit was ineffective, you have", health, "Health Left")
        elif chance >= 2 and choose == 'y':
            addHealth()
            print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land == 'd':
    print("You killed the python")
    level = 2
elif health < 1:
    print("You Died")

if land == 'f' and level == 1:
    print("A wolf has approached you")
    print("Make a move. press y to fight.")
    choose = input()
    while health > 0 and opphealth > 0:
        print_stats()
        if gold > 4:
            upgrade_strength()
        choose = input()
        flip()
        if chance == 0 and choose == 'y':
            attack()
            giveGold()
            print("hit")
        elif chance == 1 and choose == 'y':
            pythonshit()
            print("hit was ineffective, you have", health, "Health Left")
        elif chance >= 2 and choose == 'y':
            addHealth()
            print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land == 'f':
    print("You killed the wolf")
    level = 2
elif health < 1:
    print("You Died")


print("You've made it to Level 2")

if land == 'c' and level == 2:
    level_2_stats()
    print("A skeleton has approached you")
    print("Make a move. press y to fight")
    choose = input()
    while health > 0 and opphealth > 0:
        print_stats()
        if gold > 4:
            upgrade_strength2()
        choose = input()
        flip()
        if chance == 0 and choose == 'y':
            attack()
            giveGold()
            print("hit")
        elif chance == 1 and choose == 'y':
            skeletonhit()
            print("hit was ineffective, you have", health, "Health Left")
        elif chance >= 2 and choose == 'y':
            addHealth()
            print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land == 'c':
    print("You killed the skeleton")
    level = 3
elif health < 1:
    print("You Died")

    if land == 'd' and level == 2:
        level_2_stats()
        print("A golem has approached you")
        print("Make a move. press y to fight")
        choose = input()
        while health > 0 and opphealth > 0:
            print_stats()
            if gold > 4:
                upgrade_strength2()
            choose = input()
            flip()
            if chance == 0 and choose == 'y':
                attack()
                giveGold()
                print("hit")
            elif chance == 1 and choose == 'y':
                golemhit()
                print("hit was ineffective, you have", health, "Health Left")
            elif chance >= 2 and choose == 'y':
                addHealth()
                print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land == 'd':
    print("You killed the golem")
    level = 3
elif health < 1:
    print("You Died")

    if land == 'f' and level == 2:
        level_2_stats()
        print("A wild Chomp has appeared")
        print("Make a move. press y to fight")
        choose = input()
        while health > 0 and opphealth > 0:
            print_stats()
            if gold > 4:
                upgrade_strength2()
            choose = input()
            flip()
            if chance == 0 and choose == 'y':
                attack()
                giveGold()
                print("hit")
            elif chance == 1 and choose == 'y':
                chomphit()
                print("hit was ineffective, you have", health, "Health Left")
            elif chance >= 2 and choose == 'y':
                addHealth()
                print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land == 'f':
    print("You killed the Chomp")
    level = 3
elif health < 1:
    print("You Died")

    if land == 'f' and level == 3:
        level_3_stats()
        print("A totally regular knight has appeared")
        print("Make a move. press y to fight")
        choose = input()
        while health > 0 and opphealth > 0:
                print_stats()
                if gold > 4:
                    upgrade_strength3()
                choose = input()
                flip()
                if chance == 0 and choose == 'y':
                    attack()
                    giveGold()
                    print("hit")
                elif chance == 1 and choose == 'y':
                    knighthit()
                    print("hit was ineffective, you have", health, "Health Left")
                elif chance >= 2 and choose == 'y':
                    addHealth()
                    print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land == 'f':
    print("You killed the Knight")
    level = 4
elif health < 1:
    print("You Died")

    if land == 'c' and level == 3:
        level_3_stats()
        print("An Ogre has appeared")
        print("Make a move. press y to fight")
        choose = input()
        while health > 0 and opphealth > 0:
                print_stats()
                if gold > 4:
                    upgrade_strength3()
                choose = input()
                flip()
                if chance == 0 and choose == 'y':
                    attack()
                    giveGold()
                    print("hit")
                elif chance == 1 and choose == 'y':
                    ogrehit()
                    print("hit was ineffective, you have", health, "Health Left")
                elif chance >= 2 and choose == 'y':
                    addHealth()
                    print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land == 'c':
    print("You killed the Ogre.")
    level = 4
elif health < 1:
    print("You Died")

    if land == 'd' and level == 3:
        level_3_stats()
        print("A Griffin has appeared")
        print("Make a move. press y to fight")
        choose = input()
        while health > 0 and opphealth > 0:
                print_stats()
                if gold > 4:
                    upgrade_strength3()
                choose = input()
                flip()
                if chance == 0 and choose == 'y':
                    attack()
                    giveGold()
                    print("hit")
                elif chance == 1 and choose == 'y':
                    griffinhit()
                    print("hit was ineffective, you have", health, "Health Left")
                elif chance >= 2 and choose == 'y':
                    addHealth()
                    print("Enemy miss, you've healed to ", health, "Health")
if opphealth < 1 and land =='d':
    print("You killed the Griffin.")
    level = 4
elif health < 1:
    print("You Died")

if health > 0:
    print("Black Knight: (Boss)")
    print("It seems you are better at fighting than I thought (enter)")
    proceed = input()
    print("However, none shall pass(enter)")
    proceed = input()
    print("Unless...(enter)")
    proceed = input()
    print("If you can answer 3 questions correctly. (enter)")
    proceed = input()
    print("But! You will still have to duel me if you get 2 out 3 questions correct!")
    proceed = input()
    print("Are you ready? y or n")
    proceed = input()
    print("I'll take that as a yes")
    proceed = input()
    print("True or False (t or f), Barrack Obama was the 45th president of the United States")
    answer = input()
    if answer == 't':
        print("Wrong, he was the 44th president!")
    if answer == 'f':
        QnA = QnA - 1
        print("correct, he was the 44th president")
    print("next question")
    proceed = input()
    print("True or False (t or f), in Monty Python and the Holy Grail, King Arthur was played by actor Terry Gilliam")
    answer = input()
    if answer == 't':
        print("Wrong, The actor was Graham Chapman!")
    if answer == 'f':
        QnA = QnA - 1
        print("correct, the actor was played by Graham Chapman")
    print("next question")
    proceed = input()
    print("Final Question, what year did Monty Python and the Holy Grail release? (a, 1973 or b, 1975?")
    answer = input()
    if answer == 'b' and QnA == 1:
        print("You got this far, it is time!")
    if answer == 'a':
        QnA = QnA - 1
        print("Incorrect, the year was 1975")
    proceed = input()
    if level == 4 and QnA > 1:
        level_BK_stats()
        print("Fight me Coward!")
        print("Make a move. press y to fight")
        choose = input()
        while health > 0 and opphealth > 0:
                print_stats()
                if gold > 4:
                    upgrade_strength3()
                choose = input()
                flip()
                if chance == 0 and choose == 'y':
                    attack()
                    giveGold()
                    print("hit")
                elif chance == 1 and choose == 'y':
                    blackknighthit()
                    print("hit was ineffective, you have", health, "Health Left")
                elif chance >= 2 and choose == 'y':
                    addHealth()
                    print("Enemy miss, you've healed to ", health, "Health")
    else:
        print("You Died, attempting to flee the trivia.")
if opphealth < 1:
    print("You killed the Black Knight. (enter) ")
    proceed = input()
    print("Thank you for playing!")
    level = 4
elif health < 1:
    print("You Died")


