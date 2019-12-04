from discord.ext import commands,tasks

class Ratings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Define a new command
    @commands.command(
        name='update',
        description='forces the mentor ratings to update.',
        aliases=['update']
    )

    async def force_update(self, ctx):
        #Load file for mentors + post
        #load list of mentors from roles
            #Pair mentor to post
            #if mentor missing post:
                #create new post, pair mentor
            






def setup(bot):
    bot.add_cog(Basic(bot))
