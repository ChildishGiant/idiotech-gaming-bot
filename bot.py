import discord, asyncio, logging, random, time, requests, json, math

import settings, autoresponses
from commands import __time, joke, youtube, __help, roll, poll, fight, giveaways, burn, games

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

#You need to make token.txt and paste a discord bot token in it.
#using a .txt file, not a .py file to keep setup simple
with open('token.txt', 'r') as f:
    token = f.read().strip("\n")

b_Commands = {
    'rules': [settings.rulesText],
    'twitter': ['<https://twitter.com/idiotechgaming>'],
    'specs': [settings.specs],
    'reddit': ['<https://www.reddit.com/r/idiotechgaming/>'],
    'twitch': ['<https://www.twitch.tv/idiotechgaming>'],
    'patreon': ['<https://www.patreon.com/IdiotechGaming>'],
    'donate': ['<https://www.twitchalerts.com/donate/idiotechgaming>'],
    'facebook': ['<https://www.facebook.com/idiotechgaming>'],
    "links" : [settings.links],
}

@client.event
@asyncio.coroutine
def on_ready():
    print("idiotech-gaming-bot running as", client.user.name)

@client.event
@asyncio.coroutine
def on_message(message):

    #A bool for making sure only one giveaway is going at once.
    giveawayActive = False

    #Only listen to messages not from a bot.
    if not message.author.bot and message.channel.id not in settings.forbiddenChannels:

        #I use this a lot and I'm lazy.
        messagelower = message.content.lower()

        #checks for trigger words in questions
        if (message.content[-1] == "?" and ("bot" in messagelower or client.user.mentioned_in(message))):
            found = False
            for response in autoresponses.questionResponses:
                if response in messagelower:
                    found = True
                    yield from client.send_message(message.channel, random.choice(autoresponses.questionResponses[response]))
                    break

            #If no trigger words yet it is a question for the bot.
            if not found:
                #Respond with an 8ball answer.
                yield from client.send_message(message.channel, random.choice(autoresponses.eightBall))

        else:
            #checks for trigger words in messages
            for response in autoresponses.responses:
                if response in messagelower:
                    yield from client.send_message(message.channel, random.choice(autoresponses.responses[response]))
                    break



        #Checks for a command
        if message.content.startswith(settings.operator):

            yield from client.delete_message(message)

            #The command without the operator EG: giveaway start
            command = message.content.lower().lstrip(settings.operator).split()
            #If the message is just the operator / a few operators
            if len(command) < 1:
                botTalk = yield from client.send_message(message.channel, settings.helpText)
                yield from asyncio.sleep(10); yield from client.delete_message(botTalk)
                return

            #bool for keeping track of if the author is a mod.
            isMod = False

            #bool for keeping track of if the author is a backer
            isBacker = False

            for role in message.author.roles:
                if role.id in settings.modRoles:
                    isMod = True
                if role.id in settings.backerRoles:
                    isBacker = True


            if isMod:
                #Mod only commands

                if command[0] == __help.purgeHelp.call:
                    try:
                        yield from client.purge_from(message.channel, limit = int(command[1]))
                    except IndexError:
                        yield from client.send_message(message.channel, __help.purgeHelp.helpText)

                #Poll
                elif command[0] == __help.pollHelp.call:

                    if len(command) < 4:
                        botFail = yield from client.send_message(message.channel, "You need at least 3 arguments to use !poll\nfor more info use `!help poll`")
                        yield from asyncio.sleep(10)
                        yield from client.delete_message(botFail)
                    else:
                        # process arguments and sends poll data to strawpoll.me api
                        argString = poll.makeArgString(command)
                        jsondata = poll.processArguments(argString)
                        strawpoll = requests.post(settings.pollwebsite, json=jsondata)

                        botTalk = yield from client.send_message(message.channel, "Poll sucessfully created\nLink: http://www.strawpoll.me/{0}".format(strawpoll.json()['id']))

            #backer commands
            if isBacker:
                if command[0] == __help.hugHelp.call:
                    try:
                        botTalk = yield from client.send_message(message.channel, str(message.author.mention) + " :heart: " + str(command[1]))
                    except IndexError:
                        botTalk = yield from client.send_message(message.channel, __help.hugHelp.helpText)

                    yield from asyncio.sleep(10)
                    yield from client.delete_message(botTalk)

                if command[0] == __help.burnHelp.call:
                    yield from client.send_message(message.channel, burn.getBurn())

                if command[0] == "fight":

                    if len(command) < 2 or len(command) > 3:
                        botTalk = yield from client.send_message(message.channel, "Get your arguments straight, you fuck head :crossed_swords:")

                    else:
                        player1, player2 = 100, 100

                        while player1 > 0 and player2 > 0:
                            damage1 = fight.rollDamage(10)
                            damage2 = fight.rollDamage(10)
                            player1 -= math.ceil(damage1)
                            player2 -= math.ceil(damage2)
                            botTalk = yield from client.send_message(message.channel, "{0} :crossed_swords: {1}\n{0} has taken {2} damage\n{1} has taken {3} damage".format(str(message.author.mention), str(command[1]), damage1, damage2))
                            yield from asyncio.sleep(4)
                            yield from client.delete_message(botTalk)


                        if player1 < player2:
                            botTalk = yield from client.send_message(message.channel, "{0} lost the fight against {1}".format(str(message.author.mention), str(command[1])))
                        else:
                            botTalk = yield from client.send_message(message.channel, "{0} lost the fight against {1}".format(str(command[1]), str(message.author.mention)))

                            yield from asyncio.sleep(10)
                            yield from client.delete_message(botTalk)


            #@everyone commands.
            if message.content.startswith(settings.operator):

                if command[0].split()[0] == __help.timeHelp.call:

                    if len(command) == 2:
                        botTalk = yield from client.send_message(message.channel, __time.getTimezone(command[1]))

                    #if there's too many arguments
                    elif len(command) > 2:
                        botTalk = yield from client.send_message(message.channel, __help.commandError(__help.timeHelp))

                    else:
                        botTalk = yield from client.send_message(message.channel, __time.getTime())

                    yield from asyncio.sleep(10); yield from client.delete_message(botTalk)

                elif command[0] == __help.jokeHelp.call:
                    yield from client.send_message(message.channel, joke.getJoke())

                elif command[0] == __help.gamesHelp.call:
                    botTalk = yield from client.send_message(message.channel, games.fetchLatest())
                    yield from asyncio.sleep(10); yield from client.delete_message(botTalk)

                elif command[0] == __help.youtubeHelp.call:
                    botTalk = yield from client.send_message(message.channel, youtube._youtube())
                    yield from asyncio.sleep(10); yield from client.delete_message(botTalk)

                elif command[0] == __help.helpHelp.call:
                    if len(command) == 1:
                        botTalk = yield from client.send_message(message.channel, settings.helpText)
                    else:
                        botTalk = yield from client.send_message(message.channel, __help.getHelp(command[1]))

                    yield from asyncio.sleep(10); yield from client.delete_message(botTalk)

                elif command[0] == __help.rollHelp.call:
                    if len(command) < 1:
                        yield from client.send_message(message.channel, __help.commandError(__help.rollHelp))

                    elif len(command) == 1:
                        yield from client.send_message(message.channel, roll.roll(6))

                    else:
                        yield from client.send_message(message.channel, roll.roll(command[1]))

                elif message.channel.id in settings.giveawayChannels and command[0] == __help.giveawayHelp.call:
                    if len(command) > 2:

                        if isMod:
                            if command[1] == "start":
                                back = giveaways.start(command[2], message.author)
                                if back != None:
                                    yield from client.send_message(message.channel, back)

                            elif command[1] == "stop":
                                yield from client.send_message(message.channel, giveaways.stop(command[2]))


                        if command[1] == "enter":
                            back = giveaways.enter(command[2], message.author.id)
                            if back != None:
                                yield from client.send_message(message.channel, back)


                elif command[0] in b_Commands:
                    botTalk = yield from client.send_message(message.channel, b_Commands[command[0]][0])
                    yield from asyncio.sleep(10); yield from client.delete_message(botTalk)



client.run(token)
