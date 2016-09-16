import random


def getBurn():
    burns = [":man_with_turban::skin-tone-{0}: :fire:", ":nauseated_face::fire:", ":thermometer_face::fire:"]
    return random.choice(burns).format(random.randint(1,5))
