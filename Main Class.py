Health = 100
Strength = 100
Dodge = 10
Sharpness = 100
print('press a to start')
start = input()

print ("choose a character")
shellstats = [Health + 200, Strength - 30, Dodge - 9]
tankstats = [Health, Strength + 100, Dodge - 9]
ministats = [Health - 50, Strength - 10, Dodge]
print(shellstats)
character = input()
if character == 's':
    print ('you have chosen ' + character + 'hell')
elif character == 't':
    print ('you have chosen ' + character + 'ank')
elif character == 'm':
    print ('you have chosen ' + character + 'ini')

print("choose a weapon")
weapon = input()
if weapon == 's':
    print ('you have chosen ' + weapon + 'word')
elif weapon == 'sp':
    print ('you have chosen ' + weapon + 'oon')
elif weapon == 'k':
    print ('you have chosen ' + weapon + 'nife')
