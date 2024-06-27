# Tossing 3 dices 

import random
def random_dice():
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = random.randint(1,6)
    r = [x,y,z]
    return r

print("Toss the dices   ")
for x in random_dice():
    print(x)