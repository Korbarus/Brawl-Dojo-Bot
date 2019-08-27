from discord.ext import commands
import discord


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="help",
        description="The help command. You LITERALLY JUST CALLED IT.",
        aliases=["commands", "command"],
        cogs="cog"
    )
    async def help(self, ctx, cog='all'):
        embed = discord.Embed(title="**Help**", color=0xc97d7d)

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text="This bot was made by @Korbarus1384! please buy me food i haven't eaten in weeks this is a cry for help this bot is my only chance of escape")

        cogs = [c for c in self.bot.cogs.keys()]

        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            pass
        else:
            #If the user isn't an admin, the admin commands will be hidden from the help.
            cogs.pop(cogs.index("admin"))


    # If cog is not specified by the user, we list all cogs and commands

        if cog == 'all':
            for cog in cogs:
                # Get a list of all commands under each cog

                cog_commands = self.bot.get_cog(cog).get_commands()
                commands_list = ''
                for comm in cog_commands:
                    commands_list += f'**{comm.name}** - *{comm.description}*\n'

                    embed.add_field(
                        name=cog,
                        value=commands_list,
                        inline=False
                    ).add_field(
                        name='\u200b', value='\u200b', inline=False
                    )
        else:
            lower_cogs = [c.lower() for c in cogs]

            if cog.lower() in lower_cogs:
                commands_list = self.bot.get_cog(cogs[ lower_cogs.index(cog.lower()) ]).get_commands()
                help_text=''

                for command in commands_list:
                    help_text += f'```{command.name}```\n' \
                        f'**{command.description}**\n'

                    # Also add aliases, if there are any
                    if len(command.aliases) > 0:
                        help_text += f'**Aliases :** `{"`, `".join(command.aliases)}`\n\n'
                    else:
                        # Add a newline character to keep it pretty
                        # That IS the whole purpose of custom help
                        help_text += '\n'

                        # Finally the format
                    help_text += f'Format: `@{self.bot.user.name}#{self.bot.user.discriminator}' \
                            f' {command.name} {command.usage if command.usage is not None else ""}`\n\n'

                    embed.description = help_text
                embed.set_footer(text="This bot was made by @Korbarus1384! please buy me food i haven't eaten in weeks this is a cry for help this bot is my only chance of escape")

            else:
            #Notify the user of invalid cog and finish the command
                await ctx.send('Invalid command category specified.\nUse `help` command to list all categories.')
                return

        await ctx.send(embed=embed)

        return


def setup(bot):
    bot.add_cog(Misc(bot))
