modRoles = ["222359639575101442"] #The id of the mod role(s). Can be found by typing "\@MOD-ROLE-MENTION"

backerRoles = ["225042074775322624"]

forbiddenChannels = ["220502476850200595","222739924313440257"] #Channel id(s) for channels the bot is wanted in. Ids can be found by typing "\#forbidden-channel"

#What you use to trigger a command (EG: !help OR /help)
operator = "!"

#timezones to output on !time from TZ row of https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
timezones = [
"US/Pacific",
"Europe/Berlin",
"Australia/Victoria"
]

#The id of the giveaway channel(s). Can be found by typing "\#giveaway-channel"
giveawayChannels = ["222739948153995264"]

#The text displayed for !rules
rulesText = "Please see <#222739924313440257>"

#The text to say when there's already a running giveaway
giveawayOngoing = "You can't have two giveaways at once."

specs = """**Hardware & System Specs**:
Case: Corsair 650D
CPU: Intel i7 5820K
RAM: Kingston HyperX 16GB DDR4 2133 Mhz
GPU: Gigabtye G1 Gaming GTX 980
Motherboard: MSI X99A SLI Plus
SSD: Samsung 840 EVO 120GB
HDD: 2x Seagate Barracuda 2TB
OS: Windows 10
Mic: Blue Yeti"""

links = """<https://www.youtube.com/idiotechgaming>
<https://www.twitch.tv/idiotechgaming>
<https://www.patreon.com/IdiotechGaming>
<https://www.twitchalerts.com/donate/idiotechgaming>
<https://twitter.com/IdiotechGaming>
<https://www.facebook.com/idiotechgaming>
<https://www.reddit.com/r/idiotechgaming/>"""

helpText = """Here are all the current commands:
`{0}time place*` Says the time in several timezones or the one supplied
`{0}joke` Tells you a joke
`{0}roll sides*` Rolls a die with the amount of sides you ask for. Default is 6
`{0}youtube` Shows Idiotech's latest video

**Mod only commands**
`{0}giveaway start Giveaway-Name` - Starts a giveaway with the supplied name
`{0}giveaway stop` - Stops the current giveaway
`{0}bullygiant` - It bullys giant ... duh.
`{0}poll title; option 1; option 2`\nYou can set up to 10 options`

Arguments with an * after it aren't  needed""".format(operator)
