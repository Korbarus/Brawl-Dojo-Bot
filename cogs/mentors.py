from discord.ext import commands
from datetime import datetime as d
from steam import WebAPI
import requests, math, discord, gspread, oauth2client
from oauth2client.service_account import ServiceAccountCredentials
#
api = WebAPI(key="F100705340AAD1C9B521857E9FEECC14")

wepCellRange = {
    "axe":"d",
    "blasters":"e",
    "bow":"f",
    "cannon":"g",
    "gauntlets":"h",
    "hammer":"j",
    "katars":"k",
    "lance":"l",
    "orb":"l",
    "scythe":"m",
    "spear":"n",
    "sword":"o"
}

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('logins/Brawl Dojo Bot-c29a1f3656e5.json', scope)

class Mentors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="claim",
        description="Used to claim the 'Mentee' rank. This allows you to type in <#614089281207533579>.",
        aliases=["steam","link"],
        cogs="cog"
    )

    async def claim(self, ctx,link=""):
        if ctx.channel.id==614229084775383050:
            print(ctx)


            if link.startswith("https://steamcommunity.com/id/"):
                steamid = link
                print (steamid + " is the steamid")
                #First removes the start of the URL
                steamid = steamid.replace('https://steamcommunity.com/id/', '')
                #Second removes the final forward slash
                steamid = steamid.replace('/', '')
                print (steamid)

                ProcessedID = api.ISteamUser.ResolveVanityURL(vanityurl=steamid)
                print(ProcessedID)
                if ProcessedID.get('response').get("success")==1:
                    request = requests.get(("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=1470922A6B6E5C001546E51ACA5D987B&steamid=" + ProcessedID["response"].get("steamid") + "&include_appinfo=false&include_played_free_games=true&appids_filter[0]=291550"))
                    print(request.text)
                    try:
                        request = request.json()
                        minsPlayed = request["response"].get("games")
                        print(minsPlayed)
                        minsPlayed= minsPlayed[0].get("playtime_forever")
                        print(minsPlayed)
                        hrsPlayed = math.ceil((minsPlayed / 60))
                        print (hrsPlayed)

                        if (hrsPlayed >= 50):

                            role = discord.utils.get(ctx.guild.roles, name="Mentee")
                            await ctx.author.add_roles(role)
                            await ctx.message.delete()

                            confirmEmbed = discord.Embed(
                                title="\u200b",
                                color=0x00ff00,
                                description="Congratulations, " + ctx.message.author.mention + " - your steam profile has been processed. You've now been given the mentee role so you can type in <#614089281207533579>."
                            )
                            confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                            confirmEmbed.set_author(name="Congratulations, you've been confirmed!",icon_url=ctx.message.author.avatar_url)

                            await ctx.send(embed=confirmEmbed)
                            await ctx.message.delete()

                        else:
                            confirmEmbed = discord.Embed(
                                title="\u200b",
                                color=0xff0000,
                                description="Your steam profile doesn't have 50 hours in Brawlhalla yet."
                            )
                            confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                            confirmEmbed.set_author(name="You don't have enough hours yet.",icon_url=ctx.message.author.avatar_url)

                            await ctx.send(embed=confirmEmbed)

                    except TypeError:
                        confirmEmbed = discord.Embed(
                            title="\u200b",
                            color=0xff0000,
                            description="Your steam profile doesn't have 50 hours in Brawlhalla yet. You may also not have your profile set to Public, which this bot requires to work correctly."
                        )
                        confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                        confirmEmbed.set_author(name="You don't have enough hours yet.",icon_url=ctx.message.author.avatar_url)

                        await ctx.send(embed=confirmEmbed)

                elif ProcessedID.get('response').get("success")==0:
                    await ctx.send("Sorry, we couldn't process that URL. Message the Bot Dev.")

            #elif link.startswith("https://steamcommunity.com/profiles"):
            #    steamid=link
            #    print (steamid + "is the id")
            #    #First removes the start of the URL
            #    steamid = steamid.replace('https://steamcommunity.com/profiles/', '')
            #    #Second removes the final forward slash
            #    steamid = steamid.replace('/', '')
            #   print(steamid)

            #    request = requests.get(("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=1470922A6B6E5C001546E51ACA5D987B&steamid=" + steamid + "&include_appinfo=false&include_played_free_games=true&appids_filter[0]=291550"))
             #   print(request.text)
              #  try:
               #     request = request.json()
                #    minsPlayed = request["response"].get("games")
                 #   print(minsPlayed)
                  #  minsPlayed= minsPlayed[0].get("playtime_forever")
                   # print(minsPlayed)
                    #hrsPlayed = math.ceil((minsPlayed / 60))
                    #print (hrsPlayed)

            #        if (hrsPlayed >= 50):

            #            role = discord.utils.get(ctx.guild.roles, name="Mentee")
            #            await ctx.author.add_roles(role)
            #            await ctx.message.delete()

            #            confirmEmbed = discord.Embed(
            #                title="\u200b",
            #                color=0x00ff00,
            #                description="Congratulations, " + ctx.message.author.mention + " - your steam profile has been processed. You've now been given the mentee role so you can type in <#614089281207533579>."
            #            )
            #            confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
            #            confirmEmbed.set_author(name="Congratulations, you've been confirmed!",icon_url=ctx.message.author.avatar_url)

            #            await ctx.send(embed=confirmEmbed)
            #            await ctx.message.delete()

             #       else:
               #         confirmEmbed = discord.Embed(
              #              title="\u200b",
                #            color=0xff0000,
                 #           description="Your steam profile doesn't have 50 hours in Brawlhalla yet."
                  #      )
                   #     confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                    #    confirmEmbed.set_author(name="You don't have enough hours yet.",icon_url=ctx.message.author.avatar_url)

                     #   await ctx.send(embed=confirmEmbed)

              #  except TypeError:
               #     confirmEmbed = discord.Embed(
                #        title="\u200b",
                 #       color=0xff0000,
                  #      description="Your steam profile doesn't have 50 hours in Brawlhalla yet. You may also not have your profile set to Public, which this bot requires to work correctly."
                   # )
                    #confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                   # confirmEmbed.set_author(name="You don't have enough hours yet.",icon_url=ctx.message.author.avatar_url)

#                    await ctx.send(embed=confirmEmbed)




    #@commands.command(
     #   name="mentors",
     #   description="Lists the top ten mentors of a particular region. Syntax - '=mentor list eu axe",
     #   aliases= ["mentor", "top10mentors", "top10mentor"],
     #   cogs="cog"
    #)

    #async def mentors(self,ctx, region="all", weapon="all"):
    #    gc = gspread.authorize(credentials)
     #   sheet = gc.open("Brawl Dojo Mentors")
      #  if region=="all":
       #     eusheet = sheet.worksheet("raw-data-global")
        #    mentorNames = eusheet.cell()



def setup(bot):
    bot.add_cog(Mentors(bot))
