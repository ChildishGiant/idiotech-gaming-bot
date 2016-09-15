from random import randint

# Adds damage modifier to base attack, based on luck
def rollDamage(base):
    return base + ((base/4) * (randint(1, 8)))
