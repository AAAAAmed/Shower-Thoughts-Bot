# Shower-Thoughts-Bot
Just a discord bot that says some shower thoughts.

## How to run
### Making the bot account
- Go to the Discord Developer Portal and create a new app
- Create a new bot in your app and make sure to copy it's token somewhere
- Under 'OAuth2' go to 'URL Generator'
- Under 'SCOPES' select `bot` and `applications.commands`
- Under 'BOT PERMISSIONS' select 'Read Messages/View Channels' and 'Send Messages'
- Got to the generated URL and invite the bot to a Discord server
### Running the bot
- Clone this repo
- Copy your bot's token into the `token.txt` file
- Install the `discord-py-interactions` module
- Run `main.py`

That's it! You should see the bot in your server be online.
To use the bot, just type /shower_thought and optionally you can tell it how many shower thoughts you want (the default is 1).

The bot chooses a random thought from the `showerThoughts.txt` file, to add your own shower thoughts make a new line for each thought.

***If the bot says 'Too many shower thoughts at once!' that's because it reached the 2000 character limit as all the shower thoughts are sent as 1 message.**
