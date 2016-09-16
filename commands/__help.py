import settings

class helpHelp():
    #base call
    call = "help"
    #Help text
    helpText = "`{0}help [Command]` If you get this message again, check to see if you're spelling the command correctly by using `{0}help` :D".format(settings.operator)

class rollHelp():
    #base call
    call = "roll"
    #Help text
    helpText = "`{}roll [sides]` Will roll a die of that many sides. You can't have dice with less than one side because that'd just be silly.".format(settings.operator)

class jokeHelp():
    #base call
    call = "joke"
    #Help text
    helpText = "Don't be stupid"

class timeHelp():
    #base call
    call = "time"
    #Help text
    helpText = "Don't be stupid"

class youtubeHelp():
    #base call
    call = "youtube"
    #Help text
    helpText = "Don't be stupid"

class giveawayHelp():
    #base call
    call = "giveaway"
    #Help text
    helpText = "Don't be stupid"

class bullyGiantHelp():
    #base call
    call = "bullygiant"
    #Help text
    helpText = "Don't be stupid"

class hug():
    #base call
    call = "hug"
    #Help text
    helpText = "`{}hug @username`".format(settings.operator)

class pollHelp():
    #base call
    call = "poll"
    #help text
    helpText = "You need to have at least 3 arguments to use poll, the title and at least 2 options\nEG: `{}poll title; option 1; option 2`\nYou can set up to 10 options".format(settings.operator)

class fightHelp():
    #base call
    call = "fight"
    #help text
    helpText = "filler"

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

moduleLookup = {
    helpHelp.call : helpHelp,
    rollHelp.call : rollHelp,
    jokeHelp.call : jokeHelp,
    timeHelp.call : timeHelp,
    youtubeHelp.call : youtubeHelp,
    giveawayHelp.call : giveawayHelp,
    bullyGiantHelp.call : bullyGiantHelp,
    pollHelp.call : pollHelp,
    hug.call : hug,
    purgeHelp.call : purgeHelp,
    burnHelp.call : burnHelp,
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
