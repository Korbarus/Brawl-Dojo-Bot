from discord.ext import commands
from discord.ext import tasks
import discord, asyncio, random

Legends =("Bödvar", "Gnash", "Scarlet", "Lucien", "Barraza", "Ulgrim", "Wu Shang",
 "Mirage", "Artemis", "Kaya", "Zariel", "Thor", "Cassidy", "Queen Nai",
 "Thatch", "Teros", "Ember", "Diana", "Val", "Nix", "Caspian", "Isaiah",
 "Rayman", "Petra", "Orion", "Hattori", "Ada", "Brynn", "Azoth", "Jhala",
 "Ragnir", "Mordex", "Sidra", "Jiro", "Dusk", "Lord Vraxx", "Sir Roland",
 "Sentinel", "Asuri", "Koji", "Kor", "Cross", "Yumiko", "Xull", "Lin Fei",
 "Fait")

TOKEN = 'NjEyNDIzOTk0MzU1ODc1ODcx.XViTLQ.Q4d3V-LYL_uWh7392ESxH5J2qXg'
#Prefix that comes before every command, edit this if necessary

def get_prefix(client, message):

    prefixes = ['=']
    # Allow users to @mention the bot instead of using a prefix when using a command. Also optional
    # Do `return prefixes` if u don't want to allow mentions instead of prefix.
    return commands.when_mentioned_or(*prefixes)(client, message)

bot = commands.Bot(                         # Create a new bot
    command_prefix=get_prefix,              # Set the prefix
    description="Brawl Dojo's own bot.",    # Set a description for the bot
    owner_id=120251776145293312,            # Your unique User ID
    case_insensitive=True                   # Make the commands case insensitive
)


@tasks.loop(minutes=10)
async def change_status():
        current_status = discord.Game(name=("as " + random.choice(Legends)))
        print (current_status)
        await bot.change_presence(status=discord.Status.online, activity=current_status)

@bot.event
async def on_message(message):
    try:
        print(message.channel.name+"-"+message.author.name+":"+message.content)
        await bot.process_commands(message)
    except AttributeError:
        print ("DM - `"+message.author.name+":"+message.content)
    #we do not want the bot to reply to itself
    if message.author == bot.user:
        return

cogs = ['cogs.basic', 'cogs.misc','cogs.mentors',"cogs.admin"]

@bot.event
async def on_ready():                                       # Do this when the bot is logged in
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    # Print the name and ID of the bot logged in.
    bot.remove_command('help')
    # Removes the help command
    # Make sure to do this before loading the cogs
    for cog in cogs:
        bot.load_extension(cog)
        print ("loaded" + cog)
    return

@bot.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")

    newUserMessage = discord.Embed(title="** **", color=0x00ff00, description="Welcome to Brawl Dojo, please read <#612312585005694997> and <#612747304994340870> and contact our staff if you need any assistance. ")
    newUserMessage.set_thumbnail(url=str(bot.user.avatar_url))
    newUserMessage.set_author(name="Welcome to Brawl Dojo", icon_url=bot.user.avatar_url)
    newUserMessage.add_field(name="\u200b", value="To recieve mentoring, please read <#612312585005694997> and <#614229084775383050> thoroughly, especially the pins of <#614229084775383050>.e")


    await member.send(embed=newUserMessage)
    print("Sent message to " + member.name)

    # give member the steam role here
    ## to do this the bot must have 'Manage Roles' permission on server, and role to add must be lower than bot's top role
    role = discord.utils.get(member.guild.roles, name="[Guest]")
    await  member.add_roles(role)
    print("Added role '[Guest]' to " + member.name)

@change_status.before_loop
async def change_status_before_loop():
    await bot.wait_until_ready()

change_status.start()
bot.run(TOKEN, bot=True, reconnect=True)
