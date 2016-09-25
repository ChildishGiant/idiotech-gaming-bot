import random, settings

from commands import __help

currentGiveaways = {}


class giveaway:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.entrants = []

def enter(giveawayName, user):
    try:
        if user not in currentGiveaways[giveawayName].entrants:
             currentGiveaways[giveawayName].entrants.append(user)
             return "<@{0}> entered the giveaway for {1}".format(user, giveawayName)
    except KeyError:
        "PlaceHolder"

def start(name, author):

    if name not in currentGiveaways.keys():
        currentGiveaways[name] = giveaway(name, author)
        return "@here - {0} started a giveaway for {2}! Use `{3}{1} enter {2}` to enter for a chance to win!".format(author.mention, __help.giveawayHelp.call, name, settings.operator)

def stop(name):
    try:
        try:
            return "@here - <@{0}> won the giveaway for {1}".format(random.choice(currentGiveaways[name].entrants), name)
        except IndexError:
            return "No one entered your giveaway :frowning:. Ending it anyway."

        del currentGiveaways[name]

    except KeyError:
        return "I couldn't find that giveaway :frowning:"
