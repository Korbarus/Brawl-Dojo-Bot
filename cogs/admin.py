from discord.ext import commands,tasks
import discord, random
from datetime import datetime as d

class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Define a new command
    @commands.command(
        name='setmentor',
        description='Sends a message to the first user that they will be mentored by the second user.',
        aliases=['smentor',"sm"]
    )
    @commands.has_permissions(administrator=True)
    async def setmentor(self, ctx, mentee, mentor):
        mentee = await commands.MemberConverter().convert(ctx, argument=mentee)
        mentor = await commands.MemberConverter().convert(ctx, argument=mentor)

        if ctx.channel.id != 612716628089503782:
            errorEmbed = discord.Embed(title="\u200b",description="This command can only be used in <#612716628089503782>.")
            errorEmbed.set_author(name="Error processing request" , icon_url=ctx.message.author.avatar_url)
            errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
            await ctx.send(embed=errorEmbed)

        else:
            if (mentor == isinstance(mentor, discord.Member)):
                errorEmbed = discord.Embed(title="\u200b",description="You haven't specified a mentor in this command.")
                errorEmbed.set_author(name="Error processing request" , icon_url=ctx.message.author.avatar_url)
                errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
                await ctx.send(embed=errorEmbed)

            elif (mentee == isinstance(mentee, discord.Member)):
                errorEmbed = discord.Embed(title="\u200b",description="You haven't specified a mentee in this command.")
                errorEmbed.set_author(name="Error processing request" , icon_url=ctx.message.author.avatar_url)
                errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
                await ctx.send(embed=errorEmbed)
            else:
                errorEmbed = discord.Embed(title="\u200b",description="Both parties have been messaged by the bot.")
                errorEmbed.set_author(name="Request processed!" , icon_url=ctx.message.author.avatar_url)
                errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
                await ctx.send(embed=errorEmbed)


            #The message sent to the mentee
            pairmsg = ("You've been paired with: \n \n " + mentor.mention + "(@" + str(mentor) + ")")
            menteeMessage = discord.Embed(title="Your mentor request has been processed!",description=pairmsg)
            menteeMessage.set_thumbnail(url=mentor.avatar_url)
            menteeMessage.add_field(name="\u200b",value="Feel free to DM your new mentor.")
            menteeMessage.set_footer(text="Courtesy of the Brawl Dojo", icon_url=self.bot.user.avatar_url)
            await mentee.send(embed=menteeMessage)

            #The message sent to the mentee
            pairmsg = ("You've been paired with: \n \n " + mentee.mention + "(@" + str(mentee) + ")")
            mentorMessage = discord.Embed(title="You have a new mentee!",description=pairmsg)
            mentorMessage.set_thumbnail(url=mentee.avatar_url)
            mentorMessage.add_field(name="\u200b", value="Feel free to DM your new mentee.")
            mentorMessage.set_footer(text="Courtesy of the Brawl Dojo", icon_url=self.bot.user.avatar_url)
            await mentor.send(embed=mentorMessage)

            mentorrequests = await self.bot.fetch_channel(614089281207533579)

            async for elem in mentorrequests.history():
                if elem.author == mentee:
                    await elem.add_reaction(emoji="✅")

def setup(bot):
    bot.add_cog(admin(bot))
