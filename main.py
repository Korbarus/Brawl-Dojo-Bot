import discord as discord

TOKEN = 'NjEyNDIzOTk0MzU1ODc1ODcx.XViTLQ.Q4d3V-LYL_uWh7392ESxH5J2qXg'

client = discord.Client()
#Prefix that comes before every command, edit this if necessary
prefix = "="


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    print(message.channel.name+"-"+message.author.name+":"+message.content)
    if message.content.startswith("{0}hi".lower().format(prefix)):
        channel = message.channel
        msg = ("Hi, "+message.author.mention+"!")
        await channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
