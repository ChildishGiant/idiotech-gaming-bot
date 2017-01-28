# idiotech-gaming-bot
The bot used for irritating the members of Idiotech's Discord server. https://discord.gg/0z3KQXI6apyyeNOD


If you want to develop/test locally you'll need a bot user token from [here](https://discordapp.com/developers/docs/intro). Create a new file in the root folder, named `token.txt` and paste your token in. You also need a youtube API token from [here](https://console.developers.google.com/apis/dashboard). Create a new file in the root folder, named `youtubeToken.txt` and paste your youtube API token in

To install discord.py do `python3 -m pip install -U discord.py`. All other libs should be bundled with python3

Inviting bots is a bit of a hassle right now. You need to make a link to give the server owner. The format is as such:
`https://discordapp.com/oauth2/authorize?&client_id=CLIENTID&scope=bot&permissions=134704128` if you want the bot to have different permissions there is a nifty calculator located [here](https://discordapi.com/permissions.html).

Todo:
--
*Italics* are simple text commands.
- [x] Add question handling
- [x] Add polls
- [x] Add giveaways
- [x] /help
- [x] */rules*
- [x] /time
- [x] /games
- [x] */links*
- [x] */specs*
- [x] */youtube*
- [x] */twitter*
- [x] */twitch*
- [x] */patreon*
- [x] */donate*
- [x] */facebook*
- [x] */reddit*
- [x] /roll DiceSides
- [x] /fight PlayerName
- [x] /hug @Username
- [x] /help **command**
