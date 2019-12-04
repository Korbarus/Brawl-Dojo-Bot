from discord.ext import commands
import discord, random, json
from datetime import datetime as d

class admin(commands.Cog):

#Stores the id of the mirrored request and the discord tag of the original poster

    def __init__(self, bot):
        self.bot = bot

    async def setmentor(self, ctx, mentee, mentor):
        ErrorBool = False
        try:
            mentee = await commands.MemberConverter().convert(ctx, argument=mentee)
        except discord.ext.commands.errors.BadArgument:
            errorEmbed = discord.Embed(title="\u200b", description="You haven't specified a mentee in this command.")
            errorEmbed.set_author(name="Error processing request", icon_url=ctx.message.author.avatar_url)
            errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
            ErrorBool = True
            await ctx.send(embed=errorEmbed)

        try:
            mentor = await commands.MemberConverter().convert(ctx, argument=mentor)
        except discord.ext.commands.errors.BadArgument:
            errorEmbed = discord.Embed(title="\u200b", description="You haven't specified a mentor in this command.")
            errorEmbed.set_author(name="Error processing request", icon_url=ctx.message.author.avatar_url)
            errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
            ErrorBool = True
            await ctx.send(embed=errorEmbed)

        if ctx.channel.id != 612716628089503782:
            errorEmbed = discord.Embed(title="\u200b",description="This command can only be used in <#612716628089503782>.")
            errorEmbed.set_author(name="Error processing request" , icon_url=ctx.message.author.avatar_url)
            errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
            await ctx.send(embed=errorEmbed)

        elif ErrorBool == False:
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

            #open file
            with open("assets/menteelist.txt","a+") as MenteeList:
                MenteeList.write(str(mentor)+":"+str(mentee)+"\n")
            MenteeList.close()

    # Define a new command
    @commands.command(
        name='setmentor',
        description='Sends a message to the first user that they will be mentored by the second user.',
        aliases=['smentor',"sm"]
    )
    @commands.has_permissions(administrator=True)
    async def setmentor(self, ctx, mentee, mentor):
        ErrorBool = False
        try:
            mentee = await commands.MemberConverter().convert(ctx, argument=mentee)
        except discord.ext.commands.errors.BadArgument:
            errorEmbed = discord.Embed(title="\u200b", description="You haven't specified a mentee in this command.")
            errorEmbed.set_author(name="Error processing request", icon_url=ctx.message.author.avatar_url)
            errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
            ErrorBool = True
            await ctx.send(embed=errorEmbed)

        try:
            mentor = await commands.MemberConverter().convert(ctx, argument=mentor)
        except discord.ext.commands.errors.BadArgument:
            errorEmbed = discord.Embed(title="\u200b", description="You haven't specified a mentor in this command.")
            errorEmbed.set_author(name="Error processing request", icon_url=ctx.message.author.avatar_url)
            errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
            ErrorBool = True
            await ctx.send(embed=errorEmbed)

        if ctx.channel.id != 612716628089503782:
            errorEmbed = discord.Embed(title="\u200b",description="This command can only be used in <#612716628089503782>.")
            errorEmbed.set_author(name="Error processing request" , icon_url=ctx.message.author.avatar_url)
            errorEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
            await ctx.send(embed=errorEmbed)

        elif ErrorBool == False:
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

            #open file
            with open("assets/menteelist.txt","a+") as MenteeList:
                MenteeList.write(str(mentor)+":"+str(mentee)+"\n")
            MenteeList.close()


            #if key = mentor
                #add mentee tag to list of mentors
                #else:
                #add key with mentor and empty list
                #add mentee to empty list


    @commands.command(
        name='whomentor',
        description="Lists a mentor's mentees.",
        aliases=['whom', "wm","wmentor","menteelist"]
    )

    async def whomentor(self, ctx, mentor=""):
        if mentor=="":
            mentor = ctx.author
        else:
            mentor = await commands.MemberConverter().convert(ctx, argument=mentor)

        playerList = []
        with open ("assets/menteelist.txt","r+") as MenteeList:
            for line in MenteeList:
                if line.startswith(str(mentor)):
                    currLine = line.split(":")
                    currLine.remove(str(mentor))
                    playerList.append(currLine[0])
                    print(playerList)
                else:
                    pass
        MenteeList.close()

        mentees = discord.Embed(title="\u200b", description="Here's a list of the requested mentor's mentees.")
        title = (str(mentor)+"'s Mentees")
        mentees.set_author(name=title, icon_url=ctx.message.author.avatar_url)
        mentees.set_thumbnail(url=mentor.avatar_url)
        for item in playerList:
            num = ("#"+str((playerList.index(item)+1)))
            mentee=("@"+item)
            mentees.add_field(name=num, value=mentee, inline=True)

        await ctx.send(embed=mentees)



def setup(bot):
    bot.add_cog(admin(bot))
