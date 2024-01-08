from interactions import Client, Intents, listen, slash_command, SlashContext, OptionType, slash_option
import random

bot = Client(intents=Intents.DEFAULT)

thoughtsFile=open("showerThoughts.txt", "r") # This is the 'file object'
thoughts=thoughtsFile.read().splitlines() # This is the file contents
thoughtsFile.close()

def randomThought(count):
    text=''
    for _ in range(count):
        text+=f'- {thoughts[random.randint(0, len(thoughts)-1)]}\n'
    return text

@listen()
async def onReady():
    print(f"👍 READY\nThis bot was built by {bot.owner}")

@slash_command(name="shower_thought", description="Says 1 or more shower thoughts.")
@slash_option(name="count", description="Number of shower thoughts to show.", required=False, opt_type=OptionType.INTEGER)
async def showerThought(ctx: SlashContext, count: int=1):
    try: # An error is thrown if we send >2000 characters so this is required
        await ctx.send(randomThought(count))
    except:
        await ctx.send('**Too many shower thoughts at once!**')
        print('!!---   Probably too many shower thoughts at once.   ---!!')

token=open("token.txt", "r")
bot.start(token.read())
token.close()
