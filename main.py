import discord as discord

TOKEN = 'NjEyNDIzOTk0MzU1ODc1ODcx.XViTLQ.Q4d3V-LYL_uWh7392ESxH5J2qXg'

client = discord.Client()
#Prefix that comes before every command, edit this if necessary
prefix = "="


@client.event

async def on_message(message):
    print(message.channel.name+"-"+message.author.name+":"+message.content)
    channel = message.channel
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == ("{0}".format(prefix)):
        #finds the channel to send it back to
        msg = ("That's the prefix for this bot. Type '{0}help' for current commands!".format(prefix)) #msg can't handle more than 1 argument
        await channel.send(msg) #sends the message

    #Example command - checks if the message has "=hi" in it.
    if message.content.startswith("{0}hi".lower().format(prefix)):
        #finds the channel to send it back to
        msg = ("Hi, "+message.author.mention+"!") #msg can't handle more than 1 argument
        await channel.send(msg) #sends the message

    if message.content.startswith("{0}help".lower().format(prefix)):

        embed = discord.Embed(title="**Mentor Listing**", color=0x00ff00)
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.add_field(name="{0}list mentor axe".format(prefix), value="*Lists the top 10 mentors for axe globally.*", inline=True)
        embed.add_field(name="{0}list mentor axe eu".format(prefix), value="*Lists the top 10 mentors for axe in the EU.*", inline=True)
        embed.add_field(name="{0}list mentor axe na".format(prefix), value="*Lists the top 10 mentors for axe in the US.*", inline=True)
        embed.set_footer(text="This bot was made by @Korbarus1384! please buy me food i haven't eaten in weeks this is a cry for help this bot is my only chance of escape")
        await channel.send(embed=embed)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
