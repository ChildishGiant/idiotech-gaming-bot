import settings

class helpHelp():
    #base call
    call = "help"
    #Help text
    helpText = "`{0}help [command]` If you get this message again, check to see if you're spelling the command correctly by using `{0}help` :D".format(settings.operator)

class rollHelp():
    #base call
    call = "roll"
    #Help text
    helpText = "`{}roll [sides]` Will roll a die of that many sides. You can't have dice with less than one side because that'd just be silly.".format(settings.operator)

class jokeHelp():
    #base call
    call = "joke"
    #Help text
    helpText = "`{}joke` Tells a joke.".format(settings.operator)

class timeHelp():
    #base call
    call = "time"
    #Help text
    helpText = "`{0}time` Prints the time in several timezones *or*\n`{0}time [place]` Prints the time in that location (if it can)".format(settings.operator)

class youtubeHelp():
    #base call
    call = "youtube"
    #Help text
    helpText = "`{}youtube` Shows you Idiotech's latest video".format(settings.operator)

class giveawayHelp():
    #base call
    call = "giveaway"
    #Help text
    helpText = "`{0}giveaway start Giveaway-Name` - Starts a giveaway with the supplied name\n`{0}giveaway stop` - Stops the current giveaway".format(settings.operator)

class hugHelp():
    #base call
    call = "hug"
    #Help text
    helpText = "`{}hug @username` Hugs that user. ".format(settings.operator)

class pollHelp():
    #base call
    call = "poll"
    #help text
    helpText = "You need to have at least 3 arguments to use poll, the title and at least 2 options\nEG: `{0}poll title; option 1; option 2`\nYou can set up to 10 options".format(settings.operator)

class fightHelp():
    #base call
    call = "fight"
    #help text
    helpText = "`{}fight @username` Will fight that person".format(settings.operator)

class purgeHelp():
    #base call
    call = "purge"
    #help text
    helpText = "`{}purge number` Deletes that many mesages above it.".format(settings.operator)

class burnHelp():
    #base call
    call = "burn"
    #help text
    helpText = "`{}burn` Sick burn, bro".format(settings.operator)

class gamesHelp():
    #base call
    call = "games"
    #help text
    helpText = "`{}games` Lists the next 10 games to be released that Idiotech has his eyes on.".format(settings.operator)

moduleLookup = {
    helpHelp.call : helpHelp,
    rollHelp.call : rollHelp,
    jokeHelp.call : jokeHelp,
    timeHelp.call : timeHelp,
    youtubeHelp.call : youtubeHelp,
    giveawayHelp.call : giveawayHelp,
    pollHelp.call : pollHelp,
    hugHelp.call : hugHelp,
    purgeHelp.call : purgeHelp,
    burnHelp.call : burnHelp,
    gamesHelp.call : gamesHelp,
    fightHelp.call : fightHelp,
}

#Please supply a string when using this EG( __help.getHelp("roll") )
def getHelp(commandString):
    #takes a string (EG: time) and returns the help for that command
    try:
        return moduleLookup[commandString].helpText
    except KeyError:
        return commandError(helpHelp)

def commandError(command):
    return "I don't understand what you're saying\nuse `{}help {}` for more info".format(settings.operator, command.call)
