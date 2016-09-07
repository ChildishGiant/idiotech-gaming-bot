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

moduleLookup = {
    helpHelp.call : helpHelp,
    rollHelp.call : rollHelp,
    jokeHelp.call : jokeHelp,
    timeHelp.call : timeHelp,
    youtubeHelp.call : youtubeHelp,
    giveawayHelp.call : giveawayHelp
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
