from discord.ext import commands
from steam import WebAPI
import requests, math, discord, gspread
from oauth2client.service_account import ServiceAccountCredentials
#
api = WebAPI(key="F100705340AAD1C9B521857E9FEECC14")

wepArt = {
    "axe":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/d/dd/Goldforged_Axe.png?version=0c0619efad2a8b56f15fe30aa51748bb",
    "blaster":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/4/44/Goldforged_Blasters.png?version=ee18bf31d6e2e407a706d2fde5c0d0f5",
    "bow":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/7/7c/Goldforged_Bow.png?version=40df49311d548851412094feee3796e0",
    "cannon":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/7/75/Goldforged_Cannon.png?version=7be87930a3d6ad214ebbde80536bc7e4",
    "gauntlet":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/a/af/Goldforged_Gauntlets.png?version=39cccef91edc776ee550c37acb19d337",
    "hammer":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/f/fb/Goldforged_Hammer.png?version=2eb28abb96b094041f9f3254592a5fbe",
    "katar":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/b/b0/Goldforged_Katars.png?version=d865807f34f76ff3bb04ff64812f50a8",
    "lance":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/b/b6/Goldforged_Lance.png?version=239866b9258206cf9f1b51aa5f1dfe68",
    "orb":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/5/5d/Goldforged_Orb.png?version=c3d5c9c19802d14d928fa2efc814e76e",
    "scythe":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/thumb/b/b3/Goldforged_Scythe.png/1200px-Goldforged_Scythe.png?version=3ee72944401552695e8f5d69a53c0fe8",
    "spear":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/thumb/9/95/Goldforged_Spear.png/1200px-Goldforged_Spear.png?version=5653b04ec5238a42f4492cda79cc92c9",
    "sword":"https://gamepedia.cursecdn.com/brawlhalla_gamepedia/4/4a/Goldforged_Sword.png?version=738916f56c7c37b24ba6005afdc94ccb"
}

wepNameCellRange = {
    "axe":"d6:d25",
    "blaster":"i6:i25",
    "bow":"m6:m25",
    "cannon":"r6:r25",
    "gauntlet":"d29:d48",
    "hammer":"i29:i48",
    "katar":"m29:m48",
    "lance":"r29:r48",
    "orb":"d52:d71",
    "scythe":"i52:i71",
    "spear":"m52:m71",
    "sword":"r52:r71"
}

wepELOCellRange = {
    "axe":"G6:G25",
    "blaster":"k6:k25",
    "bow":"o6:o25",
    "cannon":"t6:t25",
    "gauntlet":"G29:G48",
    "hammer":"k29:k48",
    "katar":"o29:o48",
    "lance":"t29:t48",
    "orb":"G52:G71",
    "scythe":"k52:k71",
    "spear":"o52:o71",
    "sword":"t52:t71"
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
        if ctx.channel.id == 614229084775383050:
            print(link)

            if link.startswith("https://steamcommunity.com/id/") or link.startswith("http://steamcommunity.com/id/"):
                steamid = link
                print (steamid + " is the steamid")
                #First removes the start of the URL
                steamid = steamid.replace('http://steamcommunity.com/id/', '')
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
                            confirmEmbed.set_author(name="You don't have enough hours yet. You might have also not set up your privacy settings correctly.",icon_url=ctx.message.author.avatar_url)

                            await ctx.send(embed=confirmEmbed)

                    except TypeError:
                        confirmEmbed = discord.Embed(
                            title="\u200b",
                            color=0xff0000,
                            description="You do not have all elements of your profile set to Public, which this bot requires to work correctly. If you're certain this isn't the case, your steam profile may not have 50 hours in Brawlhalla yet."
                        )
                        confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                        confirmEmbed.set_author(name="Your privacy settings are incorrect.",icon_url=ctx.message.author.avatar_url)

                        await ctx.send(embed=confirmEmbed)

                elif ProcessedID.get('response').get("success")==0:
                    await ctx.send("Sorry, we couldn't process that URL. Message the Bot Dev.")

            elif link.startswith("https://steamcommunity.com/profiles/") or link.startswith("http://steamcommunity.com/profiles/"):
                confirmEmbed = discord.Embed(
                    title="\u200b",
                    color=0x00ff00,
                    description="Sorry, this type of profile link isn't supported yet. Please set up a vanity URL for your profile, as detailed in the pins."
                )

                confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                confirmEmbed.set_author(name="Sorry, this URL type isn't supported.",icon_url=ctx.message.author.avatar_url)

                await ctx.send(embed=confirmEmbed)

            elif link == "":
                confirmEmbed = discord.Embed(
                    title="\u200b",
                    color=0x00ff00,
                    description="You need to post your profile link after the command. Please see the pins for further guidance on how to use the command."
                )

                confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                confirmEmbed.set_author(name="You need to specify your profile link.",icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=confirmEmbed)

            else:
                confirmEmbed = discord.Embed(
                    title="\u200b",
                    color=0x00ff00,
                    description="You haven't written the link correctly. Please make sure you refer to the pins. The link must be the exact same format as the link shown there."
                )

                confirmEmbed.set_thumbnail(url=str(ctx.message.author.avatar_url))
                confirmEmbed.set_author(name="Wrong URL format",icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=confirmEmbed)



    @commands.command(
        name="mentors",
        description="Lists the top ten mentors of a particular region. Syntax - '=mentor list eu axe",
        aliases= ["mentor", "top10mentors", "top10mentor"],
        cogs="cog"
    )

    async def mentors(self,ctx,weapon="all", region="global"):
        gc = gspread.authorize(credentials)
        sheet = gc.open("Brawl Dojo Mentors")
        if weapon in ["blasters","katars","gauntlets"]:
            weapon = weapon[:-1]

        if region=="global":
            varSheet = sheet.worksheet("Mentors (Global)")
        elif region=="eu":
            varSheet = sheet.worksheet("Mentors (EU)")
        elif region=="na":
            varSheet = sheet.worksheet("Mentors (NA)")

        NameCellRange = varSheet.range(wepNameCellRange[weapon])
        ELOCellRange = varSheet.range(wepELOCellRange[weapon])
        top10dict= {}

        #Generates the top 10 in the form of a dictionary
        for i in range(0,11):
            top10dict[NameCellRange[i].value] = ELOCellRange[i].value
            print (ELOCellRange[i].value, NameCellRange[i].value)

        embed = discord.Embed(
            title="The top " + weapon + " mentors in the region ("+region.upper()+") are as follows:",
            color=0x00ff00,
            description="\u200b"
        )
        embed.set_author(name=("TOP " + weapon.upper() + " MENTORS (" + region.upper() + ")"),icon_url=self.bot.user.avatar_url)
        print("http://localhost" +wepArt[weapon])
        embed.set_thumbnail(url=wepArt[weapon])
        keys = list(top10dict.keys())
        keys.pop()
        print(keys)
        values = list(top10dict.values())
        values.pop()
        print(values)



        for i in range (0,10):
            try:
                embed.add_field(name="#" + str(i+1) + " -" + keys[i],value="Peak ELO: " + values[i])
            except IndexError:
                embed.add_field(name="#" + str(i+1) + " - No mentor",value="Peak ELO: N/A")

        await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Mentors(bot))
