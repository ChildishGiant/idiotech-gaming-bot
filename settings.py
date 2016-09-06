modRoles = ["222359639575101442"] #The id of the mod role(s). Can be found by typing "\@MOD-ROLE-MENTION"

#What you use to trigger a command (EG: !help OR /help)
operator = "!"

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
<> means an optional argument
[] means a required argument

`{0}time <place>` Prints the time in several timezones or the one supplied

**Mod only commands**
`{0}giveaway start [Name]` - Starts a giveaway with the supplied name
`{0}giveaway stop` - Stops the current giveaway
""".format(operator)

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
